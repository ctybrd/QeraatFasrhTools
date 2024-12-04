Sub RemoveAllVisualObjects()
    Dim shp As Shape
    Dim iShp As InlineShape
    Dim objField As Field
    
    ' Remove inline shapes (like inline images)
    For Each iShp In ActiveDocument.InlineShapes
        iShp.Delete
    Next iShp

    ' Remove floating shapes (like text boxes, SmartArt, etc.)
    For Each shp In ActiveDocument.Shapes
        shp.Delete
    Next shp

    ' Remove OLE objects (like embedded charts or equations)
    For Each objField In ActiveDocument.Fields
        If objField.Type = wdFieldEmbed Or objField.Type = wdFieldLink Then
            objField.Delete
        End If
    Next objField
End Sub
Sub RemoveImages()
    Dim img As InlineShape
    Dim shp As Shape
    
    ' Remove inline images
    For Each img In ActiveDocument.InlineShapes
        img.Delete
    Next img
    
    ' Remove floating images
    For Each shp In ActiveDocument.Shapes
        shp.Delete
    Next shp
End Sub
