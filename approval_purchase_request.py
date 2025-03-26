from abstra.forms import *
from abstra.tasks import *
from abstra.tables import *


# gets the email owner information on the tables team
def team_info_by_email(email):
    stm = select_one("team", where={"company_email": email})

    return stm


# verify if the requester is a valid user
tasks = get_tasks()
task = tasks[0]
payload = task.get_payload()

assignee_emails = payload["assignee_emails"]
purchase_request_status = payload["purchase_request_status"]
purchase_data = payload["purchase_data"]

description = purchase_data["description"]
amount = purchase_data["amount"]
quantity = purchase_data["quantity"]
reason = purchase_data["reason"]
deadline = purchase_data["deadline"]
requester_team_name = purchase_data["requester_team_name"]
requester_team_id = purchase_data["requester_team_id"]
requester_team_position = purchase_data["requester_team_position"]
purchase_request_id = purchase_data["purchase_request_id"]


approval_team_email = assignee_emails[0]

# builds the purchase approval page
approval_page = Page().display("Purchase Request Approval", size="large")\
                      .display_markdown(
    f"""

You are requested to review the following purchase request and provide your decision regarding its approval. The details of the request are as follows:
- **Description of Item(s)**: {description}
- **Total Amount**: R$ {amount}
- **Quantity Needed**: {quantity}
- **Reason for Purchase**: {reason}
- **Requested Deadline**: {deadline}
- **Submitted By**: {requester_team_name} - {requester_team_position}
- **Review Guidelines**:
1. **Budget Compatibility**: Does the requested amount align with our current budget and financial strategies?
2. **Necessity**: Is the purchase essential for the team's operations or project success?
3. **Timing**: Can the purchase wait, or is the deadline justified based on operational needs?
4. **Compliance and Procurement**: Does the request comply with our procurement policy, including seeking at least three quotes for comparison?
"""
)\
    .run(actions=["Approve", "Reject"])


if approval_page.action == "Approve":
    purchase_approved = True
else:
    purchase_approved = False
    rejection_page = Page().display("Purchase Request Rejection", size="large")\
                           .read_textarea("Reason for Rejection", key="rejection_reason")\
                           .run("Send")
    payload.update({"rejection_reason": rejection_page["rejection_reason"]})


approval_team_id = team_info_by_email(approval_team_email)["id"]

update("purchase_request_approvals", set={"approved": purchase_approved}, 
       where={"purchase_request_id": purchase_request_id, "team_id": approval_team_id})

if len(assignee_emails) > 1:
    update("purchase_request_approvals", set={"approved": purchase_approved}, 
       where={"purchase_request_id": purchase_request_id})

send_task("approval_status", payload)
task.complete()