import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil import alert

anvil.microsoft.auth.login()
if anvil.microsoft.auth.get_user_email():
  alert(f"User logged in: {anvil.microsoft.auth.get_user_email()}")
else:
  alert("Not logged in...")

