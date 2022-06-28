from re import I
from format_block import block2html, block2question
import unittest

from pyroaman.block import Block

class test_format_block(unittest.TestCase):

    def test(self):

        front = block2question("Q:测试：所有**样式**和^^多级^^内容，alias和删除双方括号，超链接，\n问题块^^第二^^行内容，还有html转义内容，还有h1~h3的样式")
        expected_front = 'Q:测试：所有<span class="bold">样式</span>和<span class="highlight">多级</span>内容，alias和删除双方括号，超链接，<br>问题块<span class="highlight">第二</span>行内容，还有html转义内容，还有h1~h3的样式'
        self.assertEqual(front, expected_front)

        front = block2question(r'Q:行内公式行间公式多行公式测试，$$V_i(0\leqslant i \leqslant n - 1)$$\n第二行$$V_i(0\leqslant i \leqslant n - 1)$$\n"$$w^{*}=\sum_{i=1}^{N} \alpha_{i}^{*} y_{i} x_{i}$$"\n"$$\begin{array}{ll}\n\underset{x \in \mathbf{R}^{n}}{\min} & f(x) \\\n\text { s.t. } & c_{i}(x) \leqslant 0, \quad i=1,2, \cdots, k \\\n& h_{j}(x)=0, \quad j=1,2, \cdots, l\n\end{array}$$"')        
        expected_front = r'Q:行内公式行间公式多行公式测试，\(V_i(0\leqslant i \leqslant n - 1)\)<br>第二行\(V_i(0\leqslant i \leqslant n - 1)\)<br>\[w^{*}=\sum_{i=1}^{N} \alpha_{i}^{*} y_{i} x_{i}\]<br>&quot;$$\begin{array}{ll}<br>\underset{x \in \mathbf{R}^{n}}{\min} &amp; f(x) \\<br>\text { s.t. } &amp; c_{i}(x) \leqslant 0, \quad i=1,2, \cdots, k \\<br>&amp; h_{j}(x)=0, \quad j=1,2, \cdots, l<br>\end{array}$$&quot;<br>&quot;$$\begin{array}{ll}<br>\underset{x \in \mathbf{R}^{n}}{\min} &amp; f(x) \\<br>\text { s.t. } &amp; c_{i}(x) \leqslant 0, \quad i=1,2, \cdots, k \\<br>&amp; h_{j}(x)=0, \quad j=1,2, \cdots, l<br>\end{array}$$&quot;'
        # self.assertEqual(front, expected_front)

        front = block2question('Q:图片测试：问题区行内"![](http://anki190912.xuexihaike.com/20200905195635.png?imageView2/2/w/250)"图片\n问题区行间图片引用\n"![](http://anki190912.xuexihaike.com/20200905195635.png?imageView2/2/w/250)"')
        expected_front=r'Q:图片测试：问题区行内<div style="text-align: center;"><img src="http://anki190912.xuexihaike.com/20200905195635.png?imageView2/2/w/250", alt=""></div>图片<br>问题区行间图片引用<br><div style="text-align: center;"><img src="http://anki190912.xuexihaike.com/20200905195635.png?imageView2/2/w/250", alt=""></div>'
        self.assertEqual(front, expected_front)

        # front = block2question('Q:多行代码块测试\n```c++\nstruct fruit {\n    string name;\n    int price;\n}```')
        # expected_front = 'Q:多行代码块测试<pre><code class="c++">struct fruit {\n    string name;\n    int price;\n}</pre></code><br>'
        # self.assertEqual(front, expected_front)

if __name__ == "__main__":
    unittest.main()