import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil import alert

if anvil.users.login_with_microsoft():
  alert(f"User logged in: {anvil.users.get_user()}")
else:
  alert("Not logged in...")

