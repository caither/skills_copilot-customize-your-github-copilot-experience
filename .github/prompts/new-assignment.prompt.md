---
agent: agent
description: 建立一個新的程式設計作業
argument-hint: 提供作業的詳細內容
---

# 建立新的程式設計作業

你的目標是為 Mergington 高中的學生產生一份新的程式設計作業。

## 步驟一：蒐集作業資訊

如果使用者尚未提供，請先詢問這份作業的主題是什麼。

## 步驟二：建立作業結構

1. 在 `assignments` 資料夾中，依照作業主題建立一個具有唯一名稱的新目錄
2. 在該目錄中建立一個名為 `README.md` 的新檔案，其結構需遵循 [`assignment-template.md`](../../templates/assignment-template.md)
3. 在 `README.md` 中填寫作業的各項細節
4. （選擇性）如果這份作業需要起始程式碼或附件，請將這些檔案加入同一個作業目錄中

## 步驟三：更新網站設定

在網站的設定檔 [config.json](../../config.json) 中更新作業清單以加入這份新作業。
對於 `dueDate` 欄位，如果沒有另外指定，請使用「目前日期加 7 天」作為繳交期限。

