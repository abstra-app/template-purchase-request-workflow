from abstra.tasks import *
from abstra.tables import *

task = get_trigger_task()
payload = task.get_payload()
purchase_data = payload["purchase_data"]

purchase_request_id = purchase_data["purchase_request_id"]

purchase_request_approvals = select("purchase_request_approvals", where={
                                    "purchase_request_id": purchase_request_id})

# sets the request status
if len(purchase_request_approvals) == 1:

    if purchase_request_approvals[0]["approved"] == True:
        approval_status = "approved"
    else:
        approval_status = "rejected"

else:

    # if any([approval["approved"] is None for approval in purchase_request_approvals]):
    #   approval_status = "pending"

    if any([approval["approved"] == False for approval in purchase_request_approvals]):
        approval_status = "rejected"

    else:
        approval_status = "approved"

condition_values = "approved,rejected".split(",")
for condition_value in condition_values:
    if approval_status == condition_value:
        send_task(approval_status, payload)
        task.complete()

