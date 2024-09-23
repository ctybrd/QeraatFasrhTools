object MasterF: TMasterF
  Left = 0
  Top = 0
  BiDiMode = bdRightToLeft
  Caption = #1575#1604#1588#1575#1588#1577' '#1575#1604#1585#1574#1610#1587#1610#1577
  ClientHeight = 583
  ClientWidth = 826
  Color = clWhite
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -13
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  ParentBiDiMode = False
  WindowState = wsMaximized
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 16
  object Splitter1: TSplitter
    Left = 0
    Top = 126
    Width = 826
    Height = 3
    Cursor = crVSplit
    Align = alTop
    ExplicitWidth = 457
  end
  object StringGridBindSourceDB1: TStringGrid
    Tag = 4
    AlignWithMargins = True
    Left = 3
    Top = 3
    Width = 820
    Height = 120
    Align = alTop
    ColCount = 4
    FixedCols = 0
    RowCount = 2
    Options = [goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goColSizing, goColMoving, goEditing, goTabs, goFixedRowDefAlign]
    TabOrder = 0
    ColWidths = (
      74
      109
      229373
      229373)
    ColAligments = (
      0
      1
      0
      0)
  end
  object StringGridBindSourceDB2: TStringGrid
    Tag = 17
    AlignWithMargins = True
    Left = 3
    Top = 132
    Width = 820
    Height = 448
    Align = alClient
    ColCount = 17
    FixedCols = 0
    RowCount = 2
    Options = [goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goColSizing, goColMoving, goEditing, goTabs, goFixedRowDefAlign]
    TabOrder = 1
    ColWidths = (
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64
      64)
    ColAligments = (
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0
      0)
  end
  object BindSourceDB1: TBindSourceDB
    DataSet = DMF.HeaderQ
    ScopeMappings = <>
    Left = 24
    Top = 56
  end
  object BindingsList1: TBindingsList
    Methods = <>
    OutputConverters = <>
    Left = 24
    Top = 8
    object LinkGridToDataSourceBindSourceDB1: TLinkGridToDataSource
      Category = 'Quick Bindings'
      DataSource = BindSourceDB1
      GridControl = StringGridBindSourceDB1
      Columns = <>
    end
    object LinkGridToDataSourceBindSourceDB2: TLinkGridToDataSource
      Category = 'Quick Bindings'
      DataSource = BindSourceDB2
      GridControl = StringGridBindSourceDB2
      Columns = <>
    end
  end
  object BindSourceDB2: TBindSourceDB
    DataSet = DMF.DetailsQ
    ScopeMappings = <>
    Left = 24
    Top = 104
  end
end
