class Solution:    
    def longestdistance(self, checkpoints):
            # Sort checkpoints from least to greatest
            #type num: list of int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            maxDist = 0
            for i in range(len(checkpoints)):
                # Traverse the list from 0 to n-i-1
                # (The last element will already be in place after first pass, so no need to re-check)
                for j in range(0, (len(checkpoints))-i-1):

                    # Swap if current element is greater than next
                    if checkpoints[j] > checkpoints[j+1]:
                        checkpoints[j], checkpoints[j+1] = checkpoints[j+1], checkpoints[j]

            
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