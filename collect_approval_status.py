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
