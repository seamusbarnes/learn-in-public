# Learn in Public

This repo is a semi-personal, public record of my software development learning journey. It was inspired heavily by [swyx](https://x.com/swyx)'s advice to ["learn in public"](https://gist.github.com/swyxio/9720bd4a30606ca3ffb8d407113c0fe5), which encourages the learner (me) to think deeply about what they are learning, and maybe can help someone on a similar path in the future. I will be focusing on documenting purely for myself for the time beging, as I don't expect anyone else to care, but the point is to produce content publicly, rather than simply consume it privately.

If I am working on something that can be public, or going through a course or lecture/video series, I will keep track of it here.

# The Story so Far

I have spent about a year on and off learning programming (almost exclusively Python), data science and machine learning/AI. I used [leetcode](https://leetcode.com)/[neetcode](https://www.youtube.com/@NeetCode) to learn data structures and algorithms (and waste time with fun programming puzzles), [kaggle](https://www.kaggle.com/seamusbarnes) competitions to learn data science, Jeremy Howard's [fastai](https://course.fast.ai/) and Andrej Karpathy's [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) courses to learn machine learning, and messed around with other courses/projects/content here and there. I also started using Anki after reading Michael Nielsen's amazing essay [Augmenting Long-term Memory](https://augmentingcognition.com/ltm.html).

Most of my learning has been sporadic, unfocussed and distracted. When you try to learn a complex topic with lots of interconnected and mutually supporting rabbit holes, my personal experience has been that without a unifying "program" or reference, the content one learns is incredibly leaky. You might spend a few hours here and there over the course of a week on a particular project, but because it's not part of a larger program and hasn't been documented in a unifying log of sorts, it's very easy to forget all about the details. When, on the other hand, you do keep a solid log of what you have done, where and why, in a unified way, you can jump right back into that project and not be immediately blown away. You don't need a formal program like a degree or course, you can create your own program, but it must be singular, unified and well maintained. That's the only way to stay on track and keep yourself accountable (to your past self and your future self, if to no one else).

# Project List

<u>Fastai course</u>
\
I went through the part one ([Practical Deep Learning for Coders](https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU)) and part of the part two ([Deep Learning Foundations to Stable Diffusion](https://course.fast.ai/Lessons/part2.html)) of the course. I did most of the exercises and produced a few things (pet classifier and architecture classifier, hosted on [huggingface spaces](https://huggingface.co/levjam) in various states of disrepair).

_Plan_ -> Go back through the course, documenting my progress, complete relevant exercises and create a huggingface spaces hosted machine learning application (e.g. some sort of classifier).

<u>Neural Networks: Zero to Hero course</u>
\
I went through most of the course, writing out the code and doing experiments here and there. I wouldn't be able to do the whole thing from scratch and until I can do that I don't think I will be happy that I've learned the material.

_Plan_ -> Same as for the fastai course, go back through it and be able to implement it all (or almost all) from scratch.

<u>Kaggle competitions</u>
\
I have joined and competed in the following competitions:

- _[Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)_ -> Starter binary classification competition with small tabular dataset. Even though this is a "toy" competition, I learned about EDA, decision tree models (random forests and bagging), and how the pandas library works.
- _[HMS - Harmful Brain Activity Classification](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification)_ -> Competition to classify brain seizure types from electroencephalography (EEG) and spectrogram data. This was a difficult competition, way above my current capabilities, but I read a lot of forum comments about how to manipulate and work with the data. Leaderboard position: 2115 / 2767
- _[Learning Agency Lab - Automated Essay Scoring 2.0](https://www.kaggle.com/competitions/learning-agency-lab-automated-essay-scoring-2)_ -> Competition to grate high school essays based on certain criteria. I learned about feature engineering and CatBoost by following public notebooks. Leaderboard position: 811 / 2708
- _[Multi-Class Prediction of Obesity Risk](https://www.kaggle.com/competitions/playground-series-s4e2)_ -> Playground series competition season 4, episode 2. Leaderboard position: 3248 / 3589
- _[Steel Plate Defect Prediction](https://www.kaggle.com/competitions/playground-series-s4e3)_ -> Playground series competition season 4, episode 3. Leaderboard position: 1773 / 2201
- _[Regression with an Abalone Dataset](https://www.kaggle.com/competitions/playground-series-s4e4)_ -> Playground series competition season 4, episode 4. Leaderboard position: 472 / 2112
- _[Regression with a Flood Prediction Dataset](https://www.kaggle.com/competitions/playground-series-s4e5)_ -> Playground series competition season 4, episode 5. Leaderboard position: 700 / 2794
- _[Binary Classification of Insurance Cross Selling](https://www.kaggle.com/competitions/playground-series-s4e7)_ -> Playground series competition season 4, episode 7. Ongoing.

<u>Historical document digitisation</u>
\
I wanted to digitise tabular data from Ordnance Survey historic land-use records, and after trying object character recognition techniques I tried using the openai api with gpt4-o and was able to digitise large sections of the dataset relatively easily. This project has the potential to save whoever evenutally digitises this data (e.g. the Ordance Survey) hundreds of hours of tedious data entry work.

<u>Projects I want to do</u>
\
...
