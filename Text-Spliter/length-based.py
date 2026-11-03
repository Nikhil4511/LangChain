from langchain_text_splitters import CharacterTextSplitter

text = """
I actually loved the batting from Shubman and Virat bhai, it was a special inning from them. It feels awkward to receive the Man of the Match award, seeing the way Virat bhai batted, it was an outstanding inning. On what he personally enjoyed most about his bowling I think personally I liked my rhythm, to be very honest. I was very calm in my rhythm and just trying to bowl whatever I felt like bowling, just varying the pace, variations were superb, just reading the batters, where they're going to hit me, and yeah, I found it very good in rhythm. On what this performance means after periods of being in and out of the side It always feels nice when you enjoy your bowling and that's where you achieve your best, and when you are enjoying your bowling, when you are a bit relaxed as well, then your performance comes at peak. So, sometimes it feels to get that confidence back, you have to have a bowling spell like this, definitely, you grow your confidence. I still believe there's a lot to improve as a spinner and I believe the rhythm, it's all about your flow, bowling flow, and when you are comfortable and when you are in good flow, then everything looks so good.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result = splitter.split_text(text)
print(result)