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
  Font.Height = -15
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  ParentBiDiMode = False
  WindowState = wsMaximized
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 18
  object Spltr: TSplitter
    AlignWithMargins = True
    Left = 3
    Top = 276
    Width = 820
    Height = 3
    Cursor = crVSplit
    Align = alTop
    Color = 2823171
    ParentColor = False
    ExplicitLeft = 0
    ExplicitTop = 126
    ExplicitWidth = 457
  end
  object HGrd: TStringGrid
    Tag = 4
    AlignWithMargins = True
    Left = 3
    Top = 88
    Width = 820
    Height = 182
    Align = alTop
    BorderStyle = bsNone
    ColCount = 4
    FixedCols = 0
    RowCount = 2
    Options = [goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goColSizing, goColMoving, goEditing, goTabs, goFixedRowDefAlign]
    TabOrder = 0
    OnDrawCell = HGrdDrawCell
    ColWidths = (
      404
      84
      2044
      2044)
    ColAligments = (
      0
      1
      0
      0)
  end
  object DGrd: TStringGrid
    Tag = 17
    AlignWithMargins = True
    Left = 3
    Top = 285
    Width = 820
    Height = 264
    Align = alClient
    BiDiMode = bdRightToLeft
    BorderStyle = bsNone
    ColCount = 17
    FixedCols = 0
    RowCount = 2
    Options = [goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goColSizing, goColMoving, goEditing, goTabs, goFixedRowDefAlign]
    ParentBiDiMode = False
    TabOrder = 1
    OnDrawCell = HGrdDrawCell
    ExplicitTop = 279
    ExplicitHeight = 263
    ColWidths = (
      84
      84
      84
      84
      124
      364
      324
      124
      106
      106
      124
      364
      89
      84
      84
      84
      84)
    ColAligments = (
      1
      1
      1
      1
      0
      0
      0
      0
      1
      1
      0
      0
      1
      1
      0
      1
      1)
  end
  object Panel1: TPanel
    AlignWithMargins = True
    Left = 3
    Top = 3
    Width = 820
    Height = 41
    Align = alTop
    BevelOuter = bvNone
    Caption = #1575#1604#1588#1575#1588#1577' '#1575#1604#1585#1574#1610#1587#1610#1577
    Color = 2823171
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWhite
    Font.Height = -16
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentBackground = False
    ParentFont = False
    TabOrder = 2
  end
  object CondPnl: TGridPanel
    AlignWithMargins = True
    Left = 3
    Top = 50
    Width = 820
    Height = 32
    Align = alTop
    BevelOuter = bvNone
    ColumnCollection = <
      item
        Value = 23.333000000000000000
      end
      item
        Value = 10.000000000000000000
      end
      item
        Value = 23.333000000000000000
      end
      item
        Value = 10.000000000000000000
      end
      item
        Value = 23.333000000000000000
      end
      item
        Value = 10.001000000000000000
      end>
    ControlCollection = <
      item
        Column = 0
        Control = QuareesEdt
        Row = 0
      end
      item
        Column = 1
        Control = Label1
        Row = 0
      end
      item
        Column = 2
        Control = SubjectEdt
        Row = 0
      end
      item
        Column = 3
        Control = Label2
        Row = 0
      end
      item
        Column = 4
        Control = ReadingEdt
        Row = 0
      end
      item
        Column = 5
        Control = Label3
        Row = 0
      end>
    RowCollection = <
      item
        Value = 100.000000000000000000
      end>
    ShowCaption = False
    TabOrder = 3
    object QuareesEdt: TEdit
      AlignWithMargins = True
      Left = 3
      Top = 3
      Width = 185
      Height = 26
      Align = alClient
      TabOrder = 0
      OnChange = ReadingEdtChange
      ExplicitLeft = 352
      ExplicitTop = 8
      ExplicitWidth = 121
    end
    object Label1: TLabel
      AlignWithMargins = True
      Left = 194
      Top = 3
      Width = 76
      Height = 26
      Align = alClient
      Alignment = taCenter
      Caption = 'Quarees'
      Layout = tlCenter
      ExplicitLeft = 162
      ExplicitWidth = 55
      ExplicitHeight = 18
    end
    object SubjectEdt: TEdit
      AlignWithMargins = True
      Left = 276
      Top = 3
      Width = 186
      Height = 26
      Align = alClient
      TabOrder = 1
      OnChange = ReadingEdtChange
      ExplicitLeft = 352
      ExplicitTop = 8
      ExplicitWidth = 121
    end
    object Label2: TLabel
      AlignWithMargins = True
      Left = 468
      Top = 3
      Width = 76
      Height = 26
      Align = alClient
      Alignment = taCenter
      Caption = 'Subject'
      Layout = tlCenter
      ExplicitLeft = 435
      ExplicitWidth = 48
      ExplicitHeight = 18
    end
    object ReadingEdt: TEdit
      AlignWithMargins = True
      Left = 550
      Top = 3
      Width = 185
      Height = 26
      Align = alClient
      TabOrder = 2
      OnChange = ReadingEdtChange
      ExplicitLeft = 352
      ExplicitTop = 8
      ExplicitWidth = 121
    end
    object Label3: TLabel
      AlignWithMargins = True
      Left = 741
      Top = 3
      Width = 76
      Height = 26
      Align = alClient
      Alignment = taCenter
      Caption = 'Reading'
      Layout = tlCenter
      ExplicitLeft = 708
      ExplicitWidth = 51
      ExplicitHeight = 18
    end
  end
  object GridPanel1: TGridPanel
    AlignWithMargins = True
    Left = 3
    Top = 555
    Width = 820
    Height = 25
    Align = alBottom
    BevelOuter = bvNone
    ColumnCollection = <
      item
        Value = 25.000000000000000000
      end
      item
        Value = 25.000000000000000000
      end
      item
        Value = 25.000000000000000000
      end
      item
        Value = 25.000000000000000000
      end>
    ControlCollection = <
      item
        Column = 0
        ColumnSpan = 3
        Control = StatusBar
        Row = 0
      end
      item
        Column = 3
        Control = CountPnl
        Row = 0
      end>
    RowCollection = <
      item
        Value = 100.000000000000000000
      end>
    ShowCaption = False
    TabOrder = 4
    ExplicitLeft = 8
    object StatusBar: TPanel
      AlignWithMargins = True
      Left = 0
      Top = 0
      Width = 612
      Height = 25
      Margins.Left = 0
      Margins.Top = 0
      Margins.Bottom = 0
      Align = alClient
      BevelOuter = bvNone
      BiDiMode = bdLeftToRight
      Color = 2823171
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWhite
      Font.Height = -12
      Font.Name = 'Tahoma'
      Font.Style = []
      ParentBiDiMode = False
      ParentBackground = False
      ParentFont = False
      TabOrder = 0
    end
    object CountPnl: TPanel
      AlignWithMargins = True
      Left = 618
      Top = 0
      Width = 202
      Height = 25
      Margins.Top = 0
      Margins.Right = 0
      Margins.Bottom = 0
      Align = alClient
      BevelOuter = bvNone
      Caption = #1593#1583#1583' '#1575#1604#1576#1581#1579
      Color = 2823171
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWhite
      Font.Height = -13
      Font.Name = 'Tahoma'
      Font.Style = [fsBold]
      ParentBackground = False
      ParentFont = False
      TabOrder = 1
      ExplicitTop = -3
    end
  end
  object HQ: TADOQuery
    Connection = DB
    CursorType = ctStatic
    Parameters = <>
    SQL.Strings = (
      
        'SELECT reading, count(*) count, group_concat(DISTINCT sub_subjec' +
        't) subject, '
      'group_concat(DISTINCT qarees) qarees'
      'FROM quran_data'
      'WHERE done IS NULL AND r5_2 IS NULL'
      'GROUP BY reading'
      'ORDER BY count(*) DESC')
    Left = 16
    Top = 64
    object HQreading: TWideMemoField
      DisplayLabel = 'Reading'
      DisplayWidth = 50
      FieldName = 'reading'
      BlobType = ftWideMemo
    end
    object HQcount: TIntegerField
      DisplayLabel = 'Count'
      FieldName = 'count'
    end
    object HQsubject: TWideStringField
      DisplayLabel = 'Sub Subjects'
      DisplayWidth = 45
      FieldName = 'subject'
      Size = 255
    end
    object HQqarees: TWideStringField
      DisplayLabel = 'Qarees'
      DisplayWidth = 45
      FieldName = 'qarees'
      Size = 255
    end
  end
  object HDS: TDataSource
    DataSet = HQ
    Left = 48
    Top = 64
  end
  object DDS: TDataSource
    DataSet = DQ
    OnDataChange = DDSDataChange
    Left = 48
    Top = 112
  end
  object DQ: TADOQuery
    Connection = DB
    CursorType = ctStatic
    DataSource = HDS
    Parameters = <
      item
        Name = 'reading'
        Attributes = [paNullable, paLong]
        DataType = ftWideMemo
        Size = 43
        Value = #1576#1578#1581#1602#1610#1602' '#1575#1604#1607#1605#1586#1577' '#1575#1604#1571#1608#1604#1609' '#1608#1578#1587#1607#1610#1604' '#1575#1604#1607#1605#1586#1577' '#1575#1604#1579#1575#1606#1610#1577'.'
      end>
    SQL.Strings = (
      
        'SELECT aya_index, id, sora, aya, sub_subject, qarees, reading, t' +
        'ags, '
      
        'page_number1, page_number2, readingresult, qareesrest, count_wor' +
        'ds, '
      'sub_sno, resultnew, wordsno, done '
      'FROM quran_data'
      'where reading = :reading')
    Left = 16
    Top = 112
    object DQaya_index: TIntegerField
      DisplayLabel = 'Aya Index'
      FieldName = 'aya_index'
    end
    object DQid: TIntegerField
      DisplayLabel = 'ID'
      FieldName = 'id'
    end
    object DQsora: TIntegerField
      DisplayLabel = 'Sora'
      FieldName = 'sora'
    end
    object DQaya: TIntegerField
      DisplayLabel = 'Aya'
      FieldName = 'aya'
    end
    object DQsub_subject: TWideMemoField
      DisplayLabel = 'Sub Subject'
      DisplayWidth = 15
      FieldName = 'sub_subject'
      BlobType = ftWideMemo
    end
    object DQqarees: TWideMemoField
      DisplayLabel = 'Qurees'
      DisplayWidth = 45
      FieldName = 'qarees'
      BlobType = ftWideMemo
    end
    object DQreading: TWideMemoField
      DisplayLabel = 'Reading'
      DisplayWidth = 40
      FieldName = 'reading'
      BlobType = ftWideMemo
    end
    object DQtags: TWideMemoField
      DisplayLabel = 'Tags'
      DisplayWidth = 15
      FieldName = 'tags'
      BlobType = ftWideMemo
    end
    object DQpage_number1: TIntegerField
      DisplayLabel = 'Page Number 1'
      FieldName = 'page_number1'
    end
    object DQpage_number2: TIntegerField
      DisplayLabel = 'Page Number 2'
      FieldName = 'page_number2'
    end
    object DQreadingresult: TWideMemoField
      DisplayLabel = 'Reading Result'
      DisplayWidth = 15
      FieldName = 'readingresult'
      BlobType = ftWideMemo
    end
    object DQqareesrest: TWideMemoField
      DisplayLabel = 'Qarees Rest'
      DisplayWidth = 45
      FieldName = 'qareesrest'
      BlobType = ftWideMemo
    end
    object DQcount_words: TIntegerField
      DisplayLabel = 'Count Words'
      FieldName = 'count_words'
    end
    object DQsub_sno: TIntegerField
      DisplayLabel = 'Sub SNo'
      FieldName = 'sub_sno'
    end
    object DQresultnew: TWideMemoField
      DisplayLabel = 'Result New'
      FieldName = 'resultnew'
      BlobType = ftWideMemo
    end
    object DQwordsno: TIntegerField
      DisplayLabel = 'Word SNo'
      FieldName = 'wordsno'
    end
    object DQDone: TIntegerField
      FieldName = 'Done'
    end
  end
  object BindSourceDB1: TBindSourceDB
    DataSet = HQ
    ScopeMappings = <>
    Left = 48
    Top = 160
  end
  object BindingsList1: TBindingsList
    Methods = <>
    OutputConverters = <>
    Left = 16
    Top = 160
    object LinkGridToDataSourceBindSourceDB1: TLinkGridToDataSource
      Category = 'Quick Bindings'
      DataSource = BindSourceDB1
      GridControl = HGrd
      Columns = <>
    end
    object LinkGridToDataSourceBindSourceDB2: TLinkGridToDataSource
      Category = 'Quick Bindings'
      DataSource = BindSourceDB2
      GridControl = DGrd
      Columns = <>
    end
  end
  object BindSourceDB2: TBindSourceDB
    DataSet = DQ
    ScopeMappings = <>
    Left = 80
    Top = 160
  end
  object DB: TADOConnection
    ConnectionString = 
      #39'Provider=MSDASQL.1;Driver=SQLite3 ODBC Driver;Database=E:\Wursh' +
      'a\QeraatFasrhTools\QeraatSearch\Tags Editor\Win32\Debug\qeraat_d' +
      'ata_simple.db;'
    LoginPrompt = False
    AfterConnect = DBAfterConnect
    Left = 16
    Top = 16
  end
end
