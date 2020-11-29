import RPi.GPIO as GPIO
import time
import random


'''GPIO.setwarnings(False)'''
redLEDLight = 4
greenLEDLight = 17
blueLEDLight = 27
s2 = 5
s3 = 6
signal = 13
NUM_CYCLES = 10
ClassificationColorList = ['BLUE','RED','RED','GREEN','BLUE','GREEN','BLUE','RED','GREEN']
listOfAvailabaleColors = ['RED','BLUE', 'GREEN']
colorAList = []
colorBList = []
colorCList = []
colorGuessedByAI = []
wasColorCorrect = []

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(redLEDLight, GPIO.OUT)
  GPIO.setup(greenLEDLight, GPIO.OUT)
  GPIO.setup(blueLEDLight, GPIO.OUT)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("Setup Complete!")
  
def pickColor(colorA, colorB, colorC):
    if(len(colorGuessedByAI) == 0):
        guessedColor = random.choice(listOfAvailabaleColors)
        if(guessedColor == ClassificationColorList[0]):
            if(guessedColor == "RED"):
                GPIO.output(redLEDLight,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(redLEDLight, GPIO.LOW)
            elif(guessedColor == "GREEN"):
                GPIO.output(greenLEDLight, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(greenLEDLight, GPIO.LOW)
            elif(guessedColor == "BLUE"):
                GPIO.output(blueLEDLight, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(blueLEDLight, GPIO.LOW)
            colorAList.append(colorA)
            colorBList.append(colorB)
            colorCList.append(colorC)
            colorGuessedByAI.append(guessedColor)
            wasColorCorrect.append(True)
            print(colorGuessedByAI[0])
        else:
            colorAList.append(colorA)
            colorBList.append(colorB)
            colorCList.append(colorC)
            colorGuessedByAI.append(guessedColor)
            wasColorCorrect.append(False)
            print(colorGuessedByAI[0])
    elif(len(colorGuessedByAI) > 0):
        counter = 0
        for booleanValue in wasColorCorrect:
            if(booleanValue == True):
                if(colorGuessedByAI[counter] == "RED"):
                     if(colorA >= (colorAList[counter] + 1000) or colorA <= (colorAList[counter] - 1000)):
                             print(colorGuessedByAI[counter])
                             if(colorGuessedByAI[counter] == ClassificationColorList[counter + 1]):
                                    colorList.append(colorA)
                                    colorList.append(colorB)
                                    colorList,append(colorC)
                                    colorGuessedByAI.append(colorGuessedByAI[counter])
                                    wasColorCorrect.append(True)
                             else:
                                    colorList.appened(colorA)
                                    colorList.append(colorB)
                                    colorList.append(colorC)
                                    colorGuessedByAI.append(colorGuessedByAI[counter])
                                    wasColorCorrect.append(False)

                             counter = counter + 1
                elif(colorGuessedByAI[counter] == "BLUE"):
                    if(colorB >= (colorBList[counter] + 1000) or colorB <= (colorBList[counter] + 1000)):
                        print("ah")


        #compare colorA from the list to see if the number given.
    #Do the same for colorB and colorC
    #check color by 5 to 10 thousand more to 5 thousand less
    #Guess the color by the compared numbers.
    #Pray that it guesses the correct numbers.
        

def loop():
  temp = 1
  while(1):  
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES): 
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
    colorA  = NUM_CYCLES / duration   
    print("Color A: " + str(colorA))

   
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    colorB = NUM_CYCLES / duration
    print("Color B: " + str(colorB))
    

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    colorC = NUM_CYCLES / duration
    print("Color C: " + str(colorC))
    print("------------------------");
    if colorA<12000 and colorB<12000 and colorC<12000:
      print("place the object.....")
    else:
        pickColor(colorA, colorB, colorC)
    


def endprogram():
    GPIO.cleanup()

def main():
    
    setup()
    
    loop()
main() 
