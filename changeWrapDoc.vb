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