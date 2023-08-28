
import time
# Countdown timer using a basic Python statements
seconds = int(input("Enter a number in seconds: "))
nseconds = seconds * -1
print(f"Starting countdown from {seconds} seconds!")

for x in range(nseconds, 0+1):
    time.sleep(1)
    print(abs(x), end='\r')


# Countdown with 'time' function (mostly)
def countdown(t):  # --'t' is number of seconds
    while t:  # --'while t' means that 't' is still an available value
        # --'min, sec' variables have been assigned 'divmod'
        # --divmod assigns 't' to '60'(meaning there is 60 seconds in 't'(in this case))
        min, secs = divmod(t, 60)

        # --'timer' is assigned to the '{:02d}:{:02d}'(making the value needing to always had 2 characters(00:00))
        # --'.format' assigns the variables to the corresponding placeholders (left-to-right)
        timer = '{:02d}:{:02d}'.format(min, secs)

        # --'"\r"' (carriage return character) when used, instead of starting a new line,
        #        it goes back to the beginning of the current line
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Timer Complete!")


t = input("Enter the time in seconds: ")

countdown(int(t))
