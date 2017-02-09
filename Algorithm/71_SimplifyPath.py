# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
#
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        stack = []
        for elem in path_list:
            if elem == '.':
                continue
            elif elem == '..':
                if stack:
                    stack.pop()
            elif elem != '':
                stack.append(elem)
        res = ''
        for word in stack:
            res += '/' + word
        if res == '':
            res = '/'
        return res
