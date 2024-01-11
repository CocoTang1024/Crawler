from bs4 import BeautifulSoup

# Your HTML table data
html_data = """
<table data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<thead data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<th data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">Field<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">田</font></font></font></th>
<th data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">Name<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">名字</font></font></font></th>
<th data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">Source<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">源</font></font></font></th>
</tr>
</thead>
<tbody data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">ccf<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">CCF基金</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《中国计算机学会推荐国际学术会议和期刊、中文科技期刊目录-2019、计算领域高质量科技期刊分级目录》，数据集从高到低分为：A(T1), B(T2), C(T3)。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">swufe<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">斯乌夫</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《西南财经大学学术期刊目录2018》，数据集从高到低分为：A+, A, B, C。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">cufe<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">CUFE公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《中央财经大学期刊目录（2019版）》，数据集从高到低分为：AAA, AA, A。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">ssci<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">SSI公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《JCR-分区-影响因子-2022(2022.6.28).pdf》，数据集从高到低分为：Q1, Q2, Q3, Q4。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sci<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">滑雪</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《JCR-分区-影响因子-2022(2022.6.28).pdf》，数据集从高到低分为：Q1, Q2, Q3, Q4。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sciif<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">SCIIF公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《JCR-分区-影响因子-2022(2022.6.28).pdf》，easyScholar将影响因子从10, 4, 2, 1, 0分为5个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">jci<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">兔</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《JCR-分区-影响因子-2022(2022.6.28).pdf》，easyScholar将JCI指数从3, 1, 0.5, 0 分为4个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sciif5</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">由于还未收集到最新5年影响因子数据，所以仍沿用2021年的数据。easyScholar将5年影响因子从10, 4, 2, 1, 0分为5个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">ahci<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">AHCI公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《JCR-分区-影响因子-2022(2022.6.28).pdf》。该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">fdu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">FDU公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《复旦大学学位与研究生教育国内期刊指导目录（2018年1月修订）》，数据集从高到低分为：A, B。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sjtu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">上海交通大学</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《上海交通大学SCISCIE论文A档B档期刊分类目录及其他刊物等级参考(2018.5)》，数据集从高到低分为：A, B。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">xmu</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《厦门大学人文社科核心学术期刊目录（2017）》，该数据集只有一个等级：一类。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">cssci<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">CSSCI的</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《CSSCI来源期刊、扩展版目录2021-2022》。数据集从高到低分为：CSSCI， CSSCI扩展版。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">ruc<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">鲁克</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《中国人民大学核心期刊目录2017》，数据集从高到低分为：A+, A, A-, B。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">cscd<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">CSCD的</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《中国科学引文数据库来源期刊列表（2021-2022 年度）》，数据集从高到低分为： 核心库，扩展库。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">swjtu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">上海交通大学</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《西南交通大学学术期刊分级目录（2017年修订版）》，数据集从高到低分为：A++, A+, A, B+, B。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">uibe<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">对外经济贸易银行</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《对外经济贸易大学科研奖励外文核心期刊专题分类目录》,数据集从高到低分为： A, A-, B。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">pku<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">北大</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《中文核心期刊要目总览》（2020年版）》，该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">xdu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">XDU的</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《关于发布《西安电子科技大学高水平期刊目录（2021年）》的通知》，数据集从高到低分为： 一类贡献度，二类贡献度。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sdufe<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">斯杜夫</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《山东财经大学学术期刊分类目录》，数据集从高到低分为： 特类期刊, A1, A2, B, C。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">eii<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">炎症性肠病</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">EI检索</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《CPXSourceList062022.xlsx》，该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">nju<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">新增功能</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《南京大学超一流、学科群一流、SCI A区和B区期刊目录.xlsx》，数据集从高到低分为： 超一流期刊（学科群一流期刊）, A, B。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">zhongguokejihexin<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">中国科吉和信</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">中国科技核心期刊目录</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《2021年版中国科技核心期刊目录.pdf》, 该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">cqu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">CQU的</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《重庆大学人文社会科学类、自然科学类期刊分级目录》，数据集从高到低分为：A（权威期刊）， B（重要期刊）， C。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">hhu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">呵呵</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《河海大学高质量论文期刊及学术会议目录（自然科学类，不含计算机科学与技术、软件工程学科）》，数据集从高到低分为：A类，B类，C类。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">ajg<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">AJG公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《ABS-2021.pdf》英文约1700种。数据集从高到低分为：4*, 4, 3, 2, 1</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">xju<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">XJU的</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《新疆大学2020版自然科学、人文社科学术期刊目录，2021年人文社科学术期刊调整目录》。数据集从高到低分为：一区， 二区， 三区，四区， 五区。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">cug<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">CUG的</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《中国地质大学科技类、人文社科类期刊分区总汇》。数据集从高到低分为：T1, T2, T3, T4, T5。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">fms<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">调频</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">FMS管理科学高质量期刊推荐列表(2022) 。数据集从高到低分为：A(T1), B(T2), C, D。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">scu<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">SCU公司</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《四川大学-高质量科技期刊及学术会议分级参考方案（暂行）-2021年4月.xlsx》。数据集从高到低分为：A, A-, B, C, D, E。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">utd24<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">曼联24</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《互联网公开收集》， 该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">ft50<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">FT50型</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《互联网公开收集》 ，该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sciUp<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">sciUp（科学Up）</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">中科院升级版</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">微信小程序：《中科院文献情报分区中心表2022年12月最新》数据集从高到低分为1区，2区，3区，4区。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sciBase<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">滑雪基地</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">中科院基础版</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">微信小程序：《中科院文献情报分区中心表2021年12月最新》数据集从高到低分为1区，2区，3区，4区。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">sciwarn<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">科学警告</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">中科院预警</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《国际期刊预警名单(试行)-2021.12.31》 ，该数据集只有一个等级。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">cju</td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《长江大学自然科学高质量期刊（中国期刊）分级目录（2021版）.pdf》数据集从高到低分为T1, T2, T3。</td>
</tr>
<tr data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8" data-immersive-translate-paragraph="1">zju<font class="notranslate immersive-translate-target-wrapper" lang="zh-CN" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-mask immersive-translate-target-translation-inline-wrapper-theme-mask immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-mask-inner" data-immersive-translate-translation-element-mark="1">圭</font></font></font></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8"></td>
<td data-immersive-translate-walked="a88a170a-7fe1-4b18-aa0f-9b7f3cc41ef8">《浙江大学国内学术期刊分级目录指南·2020版.pdf》数据集从高到低分为国内一级学术期刊，国内一级核心期刊。</td>
</tr>
</tbody>
</table>
"""

# 解析 HTML 内容
soup = BeautifulSoup(html_data, 'html.parser')

# 查找所有包含 "paragraph" 属性为 "1" 的 <td> 元素
td_elements = soup.find_all('td', {'data-immersive-translate-paragraph': '1'})

# 提取每个 <td> 元素中的内容
content_list = [td.contents[0].strip() if td.contents else '' for td in td_elements]

# 将内容用逗号分隔成字符串
formatted_content = ', '.join(content_list)

# 打印最终的格式化内容
print(formatted_content)
