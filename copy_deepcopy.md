## Python中copy和deepcopy比较
>1. 代码小实例
<pre><code>
import copy
a = [1,2,3,4,['a', 'b', 'c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
</code></pre>
<p>a是一个List，表内元素a[4]也是一个列表（内部子对象）</p>
<p>b是对a的一个引用，所以a和b是完全相等的</p>
<p>第四行是浅拷贝，第五行是深拷贝</p>

>2. 如何区别copy和deepcopy
<pre><code>
a.append(5)
a[4].append("hello")
</code></pre>
<p>查看他们的值</p>
<p>
a:[1,2,3,4,['a', 'b', 'c', 'hello'], 5]
</p>
<p>
b:[1,2,3,4,['a', 'b', 'c', 'hello'], 5]
</p>
<p>
c:[1,2,3,4,['a', 'b', 'c', 'hello']]
</p>
<p>
d:[1,2,3,4,['a', 'b', 'c']]
</p>

>3. 分析
<p>我这边就分析c，c是a的浅拷贝，只拷贝父对象,因此a的子对象（['a', 'b', 'c', 'hello']）改变会影响到c</p>

>4. 注意
<p>浅拷贝产生的是一个新的对象，但是内容却是一个引用，下面举个例子 QAQ</p>
<pre><code>
aList = [1,2]
bList = aList[:] #这是利用slice进行的浅拷贝
aList[0][0] = 5
aList:[[5,2],3,4]
bList:[[5,2],3,4]
</code></pre>
<p>另外需要特别注意的是如果对象本身是不可变的，那么浅拷贝也会产生两个值</p>
<pre><code>
aList = [1,2]
bList = [:]
bList:[1,2]
aList:[1,2]
aList[1] = 111
aList:[1,111]
bList:[1,2]
</code></pre>
