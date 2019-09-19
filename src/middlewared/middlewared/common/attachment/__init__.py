from middlewared.service import ServiceChangeMixin


class FSAttachmentDelegate(ServiceChangeMixin):
    name = NotImplementedError
    title = NotImplementedError
    service = None

    def __init__(self, middleware):
        self.middleware = middleware

    async def query(self, path, enabled):
        raise NotImplementedError

    async def get_attachment_name(self, attachment):
        raise NotImplementedError

    async def delete(self, attachments):
        raise NotImplementedError

    async def toggle(self, attachments, enabled):
        raise NotImplementedError
