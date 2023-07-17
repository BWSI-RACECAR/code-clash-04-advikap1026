class Solution:    
    def longestdistance(self, checkpoints):
            # Sort checkpoints from least to greatest
            #type num: list of int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            maxDist = 0
            # for i in range(checkpoints.len):
            #      for j in range(checkpoints.len):
            #           if(i == j):
            #                continue 
            #           dist = abs(j-i)
            #           if dist > maxDist:
            #                maxDist = dist 
            # return masDist 

            for i in range(len(checkpoints)-1):
                 firstPoint = checkpoints[i]
                 secondPoint = checkpoints[i+1]
                 dist = abs(secondPoint - firstPoint)
                 if dist > maxDist:
                      maxDist = dist
            return maxDist
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.longestdistance(array)
    print(ans)

if __name__ and "__main__":
    main()