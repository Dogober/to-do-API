from rest_framework import viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status")
        due_date = self.request.query_params.get("due_date")

        if status:
            queryset = queryset.filter(status__icontains=status)

        if due_date:
            queryset = queryset.filter(due_date__date=due_date)

        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
