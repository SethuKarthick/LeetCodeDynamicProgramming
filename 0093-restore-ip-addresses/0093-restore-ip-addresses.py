class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ip_found = []

        for i in range(1, min(4, len(s))):
            currentIp = ["", "", "", ""]
            currentIp[0] = s[:i]
            if not self.isValid(currentIp[0]):
                continue
            for j in range(i+1, i+min(4, len(s)-i)):
                currentIp[1] = s[i:j]
                if not self.isValid(currentIp[1]):
                    continue
                for k in range(j+1, j+min(4, len(s)-j)):
                    currentIp[2] = s[j:k]
                    currentIp[3] = s[k:]
                    if self.isValid(currentIp[2]) and self.isValid(currentIp[3]):
                        ip_found.append(".".join(currentIp))

        return ip_found


    def isValid(self, ipString:str):
        # ipString = str(ipString)
        # stringAsInt = int(string)
        # if stringAsInt > 255:
        #     return False
        # return len(string) == len(str(stringAsInt))
        
        stringAsInt = int(ipString) 
        if stringAsInt > 255:
            return False

        return len(ipString) == len(str(stringAsInt))
