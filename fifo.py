import pandas as pd
read=pd.read_csv("r_strings.csv")
r_strings=read.columns.tolist() # List of coloumns i.e. RS1,RS2,...,RS10
def fifo():
    for frames in range(3,7): # number of frames i.e. from 3 to 6
        hitCountList = [] # List of Hit Counts for specific number of frames
        hitRatioList = [] # List of Hit Ratios for specific number of frames
        missCountList = [] # List of Miss Counts for specific number of frames
        missRatioList = [] # List of Miss Ratios for specific number of frames
        for i in r_strings:
            rs=list(read[i]) # List containing the Requested Pages
            frame=[] # List where pages wil get appended. Size = Number of frames
            hitCount=0
            missCount=0
            hitRatio=0
            missRatio=0
            position=0
            for page in rs:
                if page in frame: # if page is present in frame then hit and skip
                    hitCount = hitCount + 1
                else: # if page is not present then miss and replace
                    missCount = missCount + 1
                    if len(frame) == frames:
                        if position == frames:
                            position = 0
                        frame.pop(position)
                        frame.insert(position,page)
                        position = position + 1
                    else:
                        frame.append(page)
            # print(frame) # The last modified frameList
            print(f"Hit Count in {i} for {frames} number of frames = {hitCount}")
            print(f"Miss Count in {i} for {frames} number of frames = {missCount}")
            hitRatio = hitCount*100/len(rs)
            missRatio = missCount*100/len(rs)
            print(f"Hit Ratio in {i} for {frames} number of frames = {hitRatio}%")
            print(f"Miss Ratio in {i} for {frames} number of frames = {missRatio}%")
            hitCountList.append(hitCount)
            hitRatioList.append(hitCount/len(rs))
            missCountList.append(missCount)
            missRatioList.append(missCount/len(rs))
        # print(hitCountList)
        # print(hitRatioList)
        # print(missCountList)
        # print(missRatioList)
        averageHitCount = sum(hitCountList)/len(hitCountList)
        averageHitRatio = (sum(hitRatioList)/len(hitRatioList))*100
        averageMissCount = sum(missCountList)/len(missCountList)
        averageMissRatio = (sum(missRatioList)/len(missRatioList))*100
        print(f"Average Hit Count for {frames} number of frames = {averageHitCount:.3f}")
        print(f"Average Hit Ratio for {frames} number of frames = {averageHitRatio:.3f}%")
        print(f"Average Miss Count for {frames} number of frames = {averageMissCount:.3f}")
        print(f"Average Miss Ratio for {frames} number of frames = {averageMissRatio:.3f}%")
fifo()
