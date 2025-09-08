class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.select_related("owner")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # add IsOwnerOrReadOnly in Step 4
    http_method_names = ["put", "patch"]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        # Example: expose a flag for PATCH vs PUT (serializer can react if needed)
        ctx["partial"] = self.request.method.lower() == "patch"
        return ctx

    @transaction.atomic
    def perform_update(self, serializer):
        """
        - Business rules before/after save
        - Example: regenerate slug when title changes
        """
        instance = serializer.instance
        old_title = instance.title

        # Save first (validations already ran)
        updated = serializer.save()

        # Post-save hook (example)
        if "title" in serializer.validated_data and updated.title != old_title:
            # e.g., if you use a slug field derived from title and keep it immutable by default,
            # you could decide to update it here.
            pass

    def update(self, request, *args, **kwargs):
        """
        Handle PUT vs PATCH explicitly. DRF already passes partial=True on PATCH,
        but this shows how you might customize responses or logging.
        """
        partial = request.method.lower() == "patch"
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Optional: add a header that indicates operation type
        headers = {"X-Operation": "partial-update" if partial else "full-update"}
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
