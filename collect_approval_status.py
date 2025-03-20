from abstra.compat import use_legacy_threads
"""
Calling the use_legacy_threads function allows using
the legacy threads in versions > 3.0.0
https://abstra.io/docs/guides/use-legacy-threads/

The new way of using workflows is with tasks. Learn more
at https://abstra.io/docs/concepts/tasks/ and contact us
on any issues during your migration
"""
use_legacy_threads("scripts")

from abstra.workflows import *
from abstra.tables import *

purchase_request_id = get_data("purchase_data")["purchase_request_id"]

purchase_request_approvals = select("purchase_request_approvals", where={
                                    "purchase_request_id": purchase_request_id})

# sets the request status
if len(purchase_request_approvals) == 1:

    if purchase_request_approvals[0]["approved"] == True:
        approval_status = "approved"
    else:
        approval_status = "rejected"

else:

    if any([approval["approved"] is None for approval in purchase_request_approvals]):
        approval_status = "pending"

    elif any([approval["approved"] == False for approval in purchase_request_approvals]):
        approval_status = "rejected"

    else:
        approval_status = "approved"


set_data("approval_status", approval_status)
