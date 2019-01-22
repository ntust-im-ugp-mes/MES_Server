# 先進生產製造執行系統（Advanced MES）
</br>

## 第一階段預定設計架構（First Stage Schema）


### [生產監控]：
  
* **機台監控（Machines-Based Monitor）**  
  顯示機台的狀態參數、基本分析（包含Utilization、Yeild、OEE、TEEP等）、預定的工作排程、及其所有的再製品清單等
  
* **物料監控（Materials-Based Monitor）**   
  顯示廠內物料目前的狀態、位置、所屬程序（被誰使用或加工等）、預定流向等
  
* **程序監控（Process-Based Monitor）**   
  顯示工作程序目前的狀態（如運行進度等）、所屬的物料等
  
### [作業排程]：

* **作業排程（Process Scheduling）**   
  提供製造排程功能，自ERP接手進行產品實際加工的排程，此亦為本系統可再深入研究之處，預計提供FIFO、SJF、PS、SRT、EDD等或其整合之排程方法    
  註：第一階段以單機排程方法及強森法則為主

* **排程管理（Schedule Management）**   
  顯示目前作業排程狀態（如排程效率參數等，待補）

### [庫存管理]：

* **庫存狀態（Inventory Viewer）**    
  顯示目前庫存狀態（偏向工廠端為主）、物料清單、存量等

* **庫存分析（Inventory Analyser）**    
  提供庫存利用分析功能，如ABC級物料分類、物料數量水準監控、物料需求量預測等

### [品質管理]：
    
* **品質管制（Quality Contorl）**   
  顯示品質管制資訊，如管制圖、良率等，並提供抽樣計畫設定等功能

* **製程能力（Process Capability）**    
  顯示製程能力指標，如製程能力指數、綜合製程能力指數等

### [資料分析及決策支援]：
* 待補，如潛藏成本、潛在利益分析等
