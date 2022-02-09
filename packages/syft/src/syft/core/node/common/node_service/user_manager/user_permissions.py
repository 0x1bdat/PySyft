# stdlib
from typing import Optional

# third party
from nacl.signing import VerifyKey

# relative
from ....abstract.node_service_interface import NodeServiceInterface
from ..generic_payload.syft_message import NewSyftMessage
from ..permissions import BasePermission


class UserCanTriageRequest(BasePermission):
    # TODO: Exceptions could fail silently either depending upon the message
    # # or the permission (not sure which one, need to discuss)

    def has_permission(
        self,
        msg: NewSyftMessage,
        node: NodeServiceInterface,
        verify_key: Optional[VerifyKey],
    ):
        _allowed = (
            node.users.can_triage_requests(verify_key=verify_key)
            if verify_key
            else False
        )
        return _allowed


class IsNodeDaaEnabled(BasePermission):
    def has_permission(
        self,
        msg: NewSyftMessage,
        node: NodeServiceInterface,
        verify_key: Optional[VerifyKey],
    ) -> bool:
        msg = type("message", (object,), msg.kwargs.upcast())()  # type: ignore

        if node.setup.first(domain_name=node.name).daa and not hasattr(msg, "daa_pdf"):
            return False

        return True


class UserCanCreateUsers(BasePermission):
    def has_permission(
        self,
        msg: NewSyftMessage,
        node: NodeServiceInterface,
        verify_key: Optional[VerifyKey],
    ):

        _allowed = (
            node.users.can_create_users(verify_key=verify_key) if verify_key else False
        )

        return _allowed


class UserIsOwner(BasePermission):
    def has_permission(
        self, msg: NewSyftMessage, node: NodeServiceInterface, verify_key: VerifyKey
    ):

        user_id = msg.kwargs.upcast().get("user_id")

        if not user_id:
            return False

        _target_user = node.users.first(id=user_id)
        request_user = node.users.get_user(verify_key=verify_key)

        # If the user has role `Owner` or request user is the target user
        _is_owner = (
            node.roles.first(id=_target_user.role).name == node.roles.owner_role.name
        ) or (request_user and _target_user.id == request_user.id)

        return _is_owner
