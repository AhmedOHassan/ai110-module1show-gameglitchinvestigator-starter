# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, the UI looked clean it had a dropdown menu with difficulty settings, a text input for guesses, and a submit button. However, the hints were backward: when my guess was too high, it said "Go HIGHER!" instead of "Go LOWER!", which made the game impossible to play correctly. The score also behaved strangely, sometimes rewarding points for wrong guesses.

- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").
1. The remaining attempts were off by one.
2. The guess hints were backwards, when my guess was too high, it said "Go HIGHER!" and when it was too low, it said "Go LOWER!".
3. The secret number seemed to keep changing. I would guess the correct number and it would say I was wrong, but on the next attempt the same guess would work. It felt like every other guess was broken no matter what I entered.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
On this project, I used Claude Code (Claude AI) as my primary AI assistant to help me understand and debug the code. I used it to ask questions about Python syntax and to get explanations of how certain functions worked. At times, I also referenced GitHub Copilot for inline code suggestions while writing.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
In the guessing game, the hints were backwards, when my guess was too high, it said "Go HIGHER!" and when it was too low, it said "Go LOWER!". I asked Claude to help me find the bug, and it pointed out that the comparison conditions in the if statement were swapped. Claude suggested switching the logic so that guess > secret_number showed "Go LOWER!" and guess < secret_number showed "Go HIGHER!". I verified the fix by running the game and testing both cases, entering a number that was too high and one that was too low, and confirming the hints now matched the correct direction.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I was debugging one of the glitches, I asked Claude what might be causing the issue and it initially suggested adding a new variable to track the state, which would have made the code more complicated than necessary. When I tried implementing it, the game didn't behave correctly and the fix felt overly complex. I went back and re-read the original code more carefully, and realized the real problem was just a simple logic error.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
To decide whether a bug was really fixed, I ran the game multiple times and tested the specific scenario that was broken to see if it now behaved correctly. For example, after fixing the backwards hints, I intentionally guessed too high and too low several times to confirm both messages showed the right direction. I also played through the full game to make sure fixing one thing didn't accidentally break something else. If the output matched what I expected every time, I considered the bug fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a manual test on the guess hint logic by entering a number I knew was higher than the secret number and checking what message appeared. Before the fix, the game incorrectly printed "Go HIGHER!" when my guess was too high, which confirmed the bug was real. After swapping the conditions in the if statement, I ran the same test again and it correctly printed "Go LOWER!", showing the fix worked. This test showed me that even a small logic error, just two conditions being swapped, can completely break the user experience of a game.

- Did AI help you design or understand any tests? How?
Yes, AI helped me think about what test cases to try when checking my fixes. When I wasn't sure if my fix was fully working, I asked Claude what kinds of inputs I should test to be thorough, and it suggested testing edge cases like guessing the exact secret number, guessing the lowest possible value, and guessing the highest possible value. This helped me realize I had only been testing the most obvious case and might have missed other issues. AI didn't run the tests for me, but it helped me think more systematically about how to verify my code was correct.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
On every even-numbered attempt, the code converted the secret number to a string before comparing it to the guess. Since a number can never equal text, those guesses always failed, making it seem like the target kept changing. The number itself never actually changed, the comparison was just broken every other turn.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you interact with a Streamlit app, like clicking a button or typing something, the entire Python script reruns from top to bottom. That means all your variables would normally reset to zero. Session state is like a small notebook the app keeps on the side, so important values like your score or number of attempts get saved and survive each rerun instead of being wiped out.

- What change did you make that finally gave the game a stable secret number?
The fix was removing the code that converted it to a string on even attempts. I changed the comparison so secret always used st.session_state.secret as an integer, meaning the guess was always compared correctly regardless of which attempt it was.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit I want to keep is testing each bug fix immediately and in isolation before moving on to the next glitch. Instead of fixing everything at once and hoping it works, I tested one change at a time, which made it much easier to know exactly what fixed what. This made debugging faster and less confusing, and I'll apply the same approach in future projects.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would read and understand the AI's suggestion before applying it, instead of just copying it in and running it. On this project I sometimes accepted fixes without fully understanding why they worked, which made it harder to explain my own code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that AI-generated code can look correct and still have subtle bugs that break the experience entirely. I now see AI as a starting point that always needs to be tested and understood, not a finished product I can trust blindly.