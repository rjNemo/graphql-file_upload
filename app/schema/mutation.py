from ariadne import MutationType

from app.file.mutations.upload import mutate_upload_user_image

Mutation = MutationType()
Mutation.set_field("uploadUserImage", mutate_upload_user_image)
