class Solution(object):
    def interpret(self, command):
        command = command.replace("()","o")
        command = command.replace("(G)","G")
        command = command.replace("(al)","al")
        return command
akua = Solution()
print(akua.interpret("G()()al"))