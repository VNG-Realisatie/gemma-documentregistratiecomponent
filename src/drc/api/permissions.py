from vng_api_common.permissions import (
    MainObjAuthScopesRequired, RelatedObjAuthScopesRequired
)

from .scopes import SCOPE_DOCUMENTEN_ALLES_LEZEN


class InformationObjectAuthScopesRequired(MainObjAuthScopesRequired):
    """
    Look at the scopes required for the current action and at informatieobjecttype and vertrouwelijkheidaanduiding
    of current informatieobject and check that they are present in the AC for this client
    """
    permission_fields = ('informatieobjecttype', 'vertrouwelijkheidaanduiding')


class InformationObjectRelatedAuthScopesRequired(RelatedObjAuthScopesRequired):
    """
    Look at the scopes required for the current action and at informatieobjecttype and vertrouwelijkheidaanduiding
    of related informatieobject and check that they are present in the AC for this client
    """
    permission_fields = ('informatieobjecttype', 'vertrouwelijkheidaanduiding')
    obj_path = 'informatieobject'

    # Define the property of the ForeignKey of which the permission fields will
    # be checked
    obj_property = 'latest_version'
