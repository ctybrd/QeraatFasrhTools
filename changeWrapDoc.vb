Sub ChangeImageWrapProperty()
    Dim doc As Document
    Dim shape As InlineShape
    
    Set doc = ActiveDocument
    
    ' Loop through all inline shapes in the document
    For Each shape In doc.InlineShapes
        ' Check if the shape is an image
        If shape.Type = wdInlineShapePicture Then
            ' Change the wrap property to "Square"
            shape.Range.Select
            Selection.ShapeRange.WrapFormat.Type = wdWrapSquare
        End If
    Next shape
End Sub

Sub ChangeTextParagraphs()
    Dim doc As Document
    Dim rng As Range
    Dim para As Paragraph
    
    ' Set the document object
    Set doc = ActiveDocument
    
    ' Set the range object to the entire document
    Set rng = doc.Content
    
    ' Loop through each paragraph in the range
    For Each para In rng.Paragraphs
        ' Change the properties for the paragraph
        para.KeepTogether = True
        para.AutoFitBehavior (wdAutoFitContent)
    Next para
End Sub
