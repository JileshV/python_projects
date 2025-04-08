import pyautogui
import pyperclip
import time
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# while True:
#     c = pyautogui.position()

#     print(c)
# 1065 878 Chrome coords
# 575 212
# 1537 753
#980 780
try:

    #Clicking chrome icon on taskbar
    pyautogui.click(1065, 878)

    # drag window to copy text
    pyautogui.click(575, 212)
    time.sleep(0.5)
    pyautogui.dragRel(990, 565, duration=0.5)

    # Copying the text
    pyperclip.copy('')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    text = pyperclip.paste()

    print(text)
except Exception as e:
    print(e)

# Create Assistant service object.
authenticator = IAMAuthenticator('{apikey}') # replace with API key
assistant = AssistantV2(
    version = '2020-09-24',
    authenticator = authenticator
)
assistant.set_service_url('{url}')
assistant_id = '{assistant_id}' # replace with assistant ID