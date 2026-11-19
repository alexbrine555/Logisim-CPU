# Logisim-CPU
Worst Logisim CPU you have ever seen in your entire life

Credit to:
https://www.reddit.com/user/Barrett1506/
https://www.youtube.com/@mattbatwings

i didnt do much here, just copied Matt's scheme and remade it in Logisim
shoutout to the random reddit user for a call stack implementation, i would've spent hours on it

Two tips if someone wants to recreate the same thing:
Go with little-endian. I tried using big-endian and it messed up everything, had to throw 8 hours of work into the bin.
Go with built-in Logisim components or use Digital (https://github.com/hneemann/Digital). Logisim runs everything at once, there is no real delay between input/output anywhere unlike in actual components. Digital has a fix for this. And Logisim built-in elements are much better than creating them yourself: you won't get an "Oscillation Apparent" error in which the circuit loops and can't find a state to settle in, that's what really stopped me. I didn't find the fix.
