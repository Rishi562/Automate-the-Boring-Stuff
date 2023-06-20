import webbrowser , sys , pyperclip

sys.argv  # ['mapil','870','valencia','St.']   
#cmd line modules are stored in a list in sys.argv
#so this will look like ['mapil','870','valencia','street']

#check if cmdline args were passed

if len(sys.argv) > 1 :
    # ['mapil','870','valencia','street'] -> '870 valencia St. '
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)






