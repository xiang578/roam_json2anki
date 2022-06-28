from format_block import block2html
import unittest

class test_format_block(unittest.TestCase):

    def test(self):
        front, back = block2html(["- Q:测试：所有**样式**和^^多级^^内容，alias和删除双方括号，超链接，", "问题块^^第二^^行内容，还有html转义内容，还有h1~h3的样式","    - **加粗**和__斜体__和~~删字符~~"])

        expected_front = 'Q:测试：所有<span class="bold">样式</span>和<span class="highlight">多级</span>内容，alias和删除双方括号，超链接，<br>问题块<span class="highlight">第二</span>行内容，还有html转义内容，还有h1~h3的样式'
        self.assertEqual(front, expected_front)
        
        # expected_back = '<li><span class=""bold"">加粗</span>和<span class=""italic"">斜体</span>和<span class=""strikethrough"">删字符</span><br>答案&amp;&amp;块<span class=""italic"">第二</span>行内容</li><ul>'
        # self.assertEqual(back, expected_back)

if __name__ == "__main__":
    unittest.main()