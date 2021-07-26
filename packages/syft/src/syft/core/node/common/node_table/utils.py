# stdlib
from typing import Any
from typing import Dict

# third party
from sqlalchemy.engine import Engine

# relative
from .groups import Group
from .roles import Role
from .user import SyftUser
from .usergroup import UserGroup


def model_to_json(model: Any) -> Dict[str, Any]:
    """Returns a JSON representation of an SQLAlchemy-backed object."""
    json = {}
    for col in model.__mapper__.attrs.keys():
        if col != "hashed_password" and col != "salt":
            if col == "date" or col == "created_at" or col == "destroyed_at":
                # Cast datetime object to string
                json[col] = str(getattr(model, col))
            else:
                json[col] = getattr(model, col)

    return json


def expand_user_object(_user: SyftUser, db: Engine) -> Dict[str, Any]:
    def get_group(user_group: UserGroup) -> Group:
        query = db.session().query
        group = user_group.group
        group = query(Group).get(group)
        group = model_to_json(group)
        return group

    query = db.session().query
    user = model_to_json(_user)
    user["role"] = query(Role).get(user["role"])
    user["role"] = model_to_json(user["role"])
    user["groups"] = query(UserGroup).filter_by(user=user["id"]).all()
    user["groups"] = [get_group(user_group) for user_group in user["groups"]]

    return user


def seed_db(db: Engine) -> None:

    new_role = Role(
        name="Data Scientist",  # type: ignore
        can_triage_requests=False,  # type: ignore
        can_edit_settings=False,  # type: ignore
        can_create_users=False,  # type: ignore
        can_create_groups=False,  # type: ignore
        can_edit_roles=False,  # type: ignore
        can_manage_infrastructure=False,  # type: ignore
        can_upload_data=False,  # type: ignore
    )
    db.add(new_role)

    new_role = Role(
        name="Compliance Officer",  # type: ignore
        can_triage_requests=True,  # type: ignore
        can_edit_settings=False,  # type: ignore
        can_create_users=False,  # type: ignore
        can_create_groups=False,  # type: ignore
        can_edit_roles=False,  # type: ignore
        can_manage_infrastructure=False,  # type: ignore
        can_upload_data=False,  # type: ignore
    )
    db.add(new_role)

    new_role = Role(
        name="Administrator",
        can_triage_requests=True,  # type: ignore
        can_edit_settings=True,  # type: ignore
        can_create_users=True,  # type: ignore
        can_create_groups=True,  # type: ignore
        can_edit_roles=False,  # type: ignore
        can_manage_infrastructure=False,  # type: ignore
        can_upload_data=True,  # type: ignore
    )
    db.add(new_role)

    new_role = Role(
        name="Owner",  # type: ignore
        can_triage_requests=True,  # type: ignore
        can_edit_settings=True,  # type: ignore
        can_create_users=True,  # type: ignore
        can_create_groups=True,  # type: ignore
        can_edit_roles=True,  # type: ignore
        can_manage_infrastructure=True,  # type: ignore
        can_upload_data=True,  # type: ignore
    )
    db.add(new_role)
    db.commit()
