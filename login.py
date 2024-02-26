name = input ('Enter your first name: ')
print('Welcome,'+name.title()+ '. Please create your account details!')
username1 = input('Create username: ')
password1 = input('Create password: ')
print('Account successfully created, '+name.title()+ '. Please log into your account')
username2 = input('Enter username: ')
password2 = input('Enter Password: ')

if username1 == username2 and password1 == password2:
   print('Login successful,' +name.title()+ '. Thanks for your time.')

else:
   print('Credentials do not match, please try again.')