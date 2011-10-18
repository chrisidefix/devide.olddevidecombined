# Start an appropriate shell according to the OS name
import os
if os.name == 'nt':
	os.system('cmd')
else:
	os.system('bash')
