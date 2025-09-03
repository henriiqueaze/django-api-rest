from rest_framework import viewsets
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)
from drf_spectacular.types import OpenApiTypes

from myapp.models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @extend_schema(
        summary="Listar clientes",
        description=(
            "Retorna lista paginada de clientes. "
            "Opcionalmente filtrável por `search` (nome/email contains)."
        ),
        responses={200: ClientSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                name="search",
                description="Filtro por nome ou email (contains).",
                required=False,
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="page",
                description="Número da página (padrão: 1).",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Recuperar cliente",
        description="Retorna os detalhes de um cliente pelo seu ID (pk).",
        responses={200: ClientSerializer},
        parameters=[
            OpenApiParameter(
                name="pk",
                description="ID do cliente",
                required=True,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
            )
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Criar cliente",
        description="Cria um novo cliente. Campos obrigatórios: `name`, `email`, `birth_date`.",
        request=ClientSerializer,
        responses={201: ClientSerializer},
        examples=[
            OpenApiExample(
                "Exemplo criar cliente",
                value={"name": "Maria Silva", "email": "maria@example.com", "birth_date": "1990-05-20"},
                request_only=True
            )
        ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Atualizar cliente (PUT)",
        description="Substitui todos os campos do cliente informado pelo ID.",
        request=ClientSerializer,
        responses={200: ClientSerializer},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Atualizar parcialmente cliente (PATCH)",
        description="Atualiza parcial de campos do cliente.",
        request=ClientSerializer,
        responses={200: ClientSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Excluir cliente",
        description="Remove o cliente especificado pelo ID.",
        responses={204: None},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
