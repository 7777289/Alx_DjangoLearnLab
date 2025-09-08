from django.db import transaction
from django.urls import reverse

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        # Add extra context your serializer may need
        ctx = super().get_serializer_context()
        ctx["request_ip"] = self.request.META.get("REMOTE_ADDR")  # example
        return ctx

    @transaction.atomic
    def perform_create(self, serializer):
        """
        - Attach owner
        - Do any pre-save checks
        - Save inside an atomic transaction
        """
        # Example: ensure a user can't create more than N books per day
        # (Uncomment if you need rate-limiting-by-model)
        # today_count = Book.objects.filter(owner=self.request.user, created_at__date=date.today()).count()
        # if today_count >= 50:
        #     raise ValidationError("Daily book creation limit reached.")

        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Override to:
        - use serializer with context
        - return Location header pointing to the new resource
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = {}
        instance = serializer.instance
        if instance:
            headers["Location"] = reverse("book-detail", args=[instance.pk])

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
