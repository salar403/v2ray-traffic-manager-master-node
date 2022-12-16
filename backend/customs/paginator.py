def custom_paginator(queryset: list, serializer_data: dict):
    page = serializer_data["page"]
    per_page = serializer_data["per_page"]
    return queryset[(page - 1) * per_page : page * per_page]