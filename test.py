import re

s = "答案里面也有 ((VkVmbbB8V))"
block_ref = r"\(\((.*?)\)\)"

ret = re.findall(block_ref, s)
print(ret)