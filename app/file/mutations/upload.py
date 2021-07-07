import os
from typing import Any

from ariadne import convert_kwargs_to_snake_case
from fastapi import File, UploadFile
from graphql import GraphQLResolveInfo

from ...core.config import BASE_DIR


@convert_kwargs_to_snake_case
async def mutate_upload_user_image(
    _: Any, _info: GraphQLResolveInfo, image: UploadFile = File(...)
) -> bool:
    with open(os.path.join(BASE_DIR, "app", "database", "file.txt"), "a") as f:
        f.write(f"{image.filename}\n")
    with open(os.path.join(str(os.getcwd()), "app", "database", "file.txt"), "r") as f:
        print(f.read())

    return True
