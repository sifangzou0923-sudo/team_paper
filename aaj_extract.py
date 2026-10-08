# -*- coding: utf-8 -*-
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

OUT = r'D:\data\review_notes\aaj_papers'
os.makedirs(OUT, exist_ok=True)

papers = {
# journal articles
'RAQNAIXL': r'D:\data\zotero\storage\GAPKR5S4\Liu 等 - 2020 - Comparison of the rock breakage pressure of abrasive water jets and abrasive air jets.pdf',
'AJI3VFAH': r'D:\data\zotero\storage\XKVY6M6P\2018.9-磨料水射流与磨料气体射流破岩压力对比分析.pdf',
'KRSN4DE9': r'D:\data\zotero\storage\I9II3UIW\魏建平 等 - 2025 - 低压磨料空气射流切割硬岩评价模型及应用.pdf',
'GT2QZGMT': r'D:\data\zotero\storage\8IJ98TDX\2024.7-冰粒空气射流喷射器结构的关键参数.pdf',
'UW768JU6': r'D:\data\zotero\storage\DVCFNSS4\Yu 等 - 2025 - Research on real time measurement model and measurement system for gas concentration in extraction d.pdf',
'DEQ7KTXJ': r'D:\data\zotero\storage\AG6ZZWQ7\Wei 等 - 2025 - Effect of abrasive mass flow rate on energy efficiency in low-pressure supersonic abrasive air jet r.pdf',
'UPW2NSS4': r'D:\data\zotero\storage\WVL3DKMD\Man 等 - 2024 - Study on the key parameters of ice particle air jet ejector structure.pdf',
'8LTYLLTN': r'D:\data\zotero\storage\S8MI68H7\Chen 等 - 2025 - Effect of abrasive volume fraction on energy utilization in suspension abrasive water jets based on.pdf',
'8T6GNPRZ': r'D:\data\zotero\storage\YSWYSW32\Li 等 - 2023 - Molecular dynamics simulation and experimental study into effect of temperature on hardness of ice a.pdf',
'GXLGB47T': r'D:\data\zotero\storage\A6DBBN3S\Li 等 - 2022 - Study of a new method for the instant preparation of ice particles in ice abrasive air jet.pdf',
'PJCZ85NX': r'D:\data\zotero\storage\KXNXAX7Y\Chen 等 - 2022 - Investigation of Coal Failure Characters Based on Jet Energy and Impact Frequency During Particle Je.pdf',
'M3DUATGY': r'D:\data\zotero\storage\TNBB854M\Liu 等 - 2021 - Effect of nozzle pressure ratio on pulsation frequency of air jets used in hole drilling.pdf',
'A3A7SRCR': r'D:\data\zotero\storage\6CVN4WYH\Liu 等 - 2021 - Erosion Wear Characteristics of Rock Eroded Using Abrasive Air Jet at 90° Impingement Angle.pdf',
'M3C9PFIH': r'D:\data\zotero\storage\RCY8M2WA\Chen 等 - 2022 - Effect of nozzle pressure ratios on the flow and distribution of abrasive particles in abrasive air.pdf',
'XAKJWZF7': r'D:\data\zotero\storage\VNAD4VPG\Liu 等 - 2020 - Optimum structure of a laval nozzle for an abrasive air jet based on nozzle pressure ratio.pdf',
'A4JKWB6R': r'D:\data\zotero\storage\C4JPY4KM\2025.11-松软煤层空气射流冲孔卸压关键技术研究与应用.pdf',
'I32FGVXR': r'D:\data\zotero\storage\8J4ZLMJU\Liu 等 - 2020 - Influence of abrasive hardness on erosion wear of abrasive air jets.pdf',
'INPDPX7G': r'D:\data\zotero\storage\XTQY3CB6\2024.8-松软煤层无水化增透理论及技术发展趋势.pdf',
'L2EPYGS3': r'D:\data\zotero\storage\KC8MRIAC\Liu 等 - 2019 - Wear Mechanism of Abrasive Gas Jet Erosion on a Rock and the Effect of Abrasive Hardness on It.pdf',
'CTV5584I': r'D:\data\zotero\storage\LEBZNUUZ\2023.11-低压磨料空气射流切槽辅助TBM滚刀破岩规律.pdf',
'IL7VBVMW': r'D:\data\zotero\storage\J36NZMQT\Ranjith 等 - 2019 - Effect of abrasive mass flow on the abrasive acceleration and erosion rates of abrasive gas jets.pdf',
'TLZ6XYL6': r'D:\data\zotero\storage\EHPPKR2U\2023.10-低压超声速磨料空气射流喷嘴结构.pdf',
'ZVVIE2XJ': r'D:\data\zotero\storage\C2YSNVFQ\2023.2-后混合磨料空气射流喷嘴结构优化及破煤效果研究.pdf',
'LCN5MMP2': r'D:\data\zotero\storage\32SZZGXK\Liu 等 - 2018 - Optimal Nozzle Structure for an Abrasive Gas Jet for Rock Breakage.pdf',
'JXF8C4FR': r'D:\data\zotero\storage\78EXDUFD\2022.7-基于应力波效应的磨料射流破煤能量准则.pdf',
'RUHZDRGT': r'D:\data\zotero\storage\M56VK4SX\Liu 等 - 2018 - Analysis of the stress wave effect during coal breakage by a high-pressure abrasive air jet.pdf',
'FEYF2SXM': r'D:\data\zotero\storage\P9PYW2H6\2022.1-低压磨料空气射流破硬岩规律及特征实验研究.pdf',
'S36CH9TZ': r'D:\data\zotero\storage\7KIXIDI4\2021.7-不同膨胀比下气体射流流场结构及脉动频率.pdf',
'WAQCHK56': r'D:\data\zotero\storage\DTPN97QL\Liu 等 - 2017 - Experimental and numerical optimization of coal breakage performance parameters through abrasive gas.pdf',
'5ETKJKMZ': r'D:\data\zotero\storage\NMY5IRJU\2021.5-围压对磨料空气射流破煤深度的影响研究.pdf',
'3RVPW38T': r'D:\data\zotero\storage\FZ3VRZVB\2020.5-磨料空气射流破煤冲蚀模型研究.pdf',
'88JJD7DN': r'D:\data\zotero\storage\5LJJI7X3\Wen 等 - 2017 - Experimental research into the effects of abrasive characteristics on abrasive gas jet coal-breaking.pdf',
'YPR8IDIC': r'D:\data\zotero\storage\LT675JHM\2018.11-磨料气体射流冲蚀磨损岩石特征分析.pdf',
'HJHW27XD': r'D:\data\zotero\storage\59MNMIMB\2018.11-基于拉法尔喷嘴的磨料气体射流加速规律研究.pdf',
'59353NTH': r'D:\data\zotero\storage\63EYMNPR\2018.5-磨料属性影响高压磨料气体射流破岩效果的理论及实验研究_刘勇.pdf',
'4ZBLYPS6': r'D:\data\zotero\storage\BWMIYNFF\2017.11-磨料形状对磨料气体射流冲蚀性能的影响研究.pdf',
'9ABZQXKY': r'D:\data\zotero\storage\GMJJAWGC\2016.7-高压气体射流破煤应力波效应分析.pdf',
# theses
'PPSN58FL': r'D:\data\zotero\storage\PPSN58FL\蔡玉波-低压磨料空气射流切割硬岩效果评价及参数优化研究.pdf',
'7HWZFP4W': r'D:\data\zotero\storage\LVBVMKFQ\李志平 - 2025 - 9、李志平-低压磨料空气射流线性切割喷嘴结构优化研究.pdf',
'93BXHDLK': r'D:\data\zotero\storage\93BXHDLK\吴姣姣-冰粒空气射流冰粒即时制备与参数调控研究.pdf',
'RITR4GUF': r'D:\data\zotero\storage\RITR4GUF\李志飞-冰粒空气射流调制及表面处理实验研究.pdf',
'5SY4S6K9': r'D:\data\zotero\storage\5SY4S6K9\张涛-高压磨料气体射流冲蚀煤岩影响因素及冲蚀体积模型研究.pdf',
'UTDUE42R': r'D:\data\zotero\storage\RXPKRSNB\陈长江-高压磨料气体射流破煤应力波传播模型研究.pdf',
'4QF54AAR': r'D:\data\zotero\storage\4QF54AAR\梁博臣-磨料气体射流磨料加速机理及其分布规律研究.pdf',
'EXUWLUT4': r'D:\data\zotero\storage\Y7KUQ2JJ\张娟-膨胀比对高压磨料气体射流破煤影响规律研究.pdf',
'DM7366IF': r'D:\data\zotero\storage\FDE3SMEW\何岸-磨料气体射流破煤岩喷嘴结构优化.pdf',
'MKZV3W75': r'D:\data\zotero\storage\Z3UE7BN9\戴彪-磨料特性对磨料气体射流破煤影响的实验研究.pdf',
'YAWJ7AX5': r'D:\data\zotero\storage\YAWJ7AX5\余大炀-磨料空气射流切槽协同滚刀破岩关键参数研究.pdf',
'ZZKVG846': r'D:\data\zotero\storage\ZZKVG846\黄逸-磨料空气射流切割核容器不锈钢的参数优化研究.pdf',
}

for key, path in papers.items():
    try:
        doc = pymupdf.open(path)
        n = doc.page_count
        txt = []
        for i in range(n):
            txt.append(doc[i].get_text())
        full = '\n'.join(txt)
        with open(os.path.join(OUT, key + '.txt'), 'w', encoding='utf-8') as f:
            f.write(f'## {key} | pages={n}\n')
            f.write(full)
        print(f'{key}: pages={n}, chars={len(full)}')
        doc.close()
    except Exception as e:
        print(f'{key}: ERROR {e}')
