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
    Top = 246
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
  object HeadPnl: TPanel
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
    TabOrder = 0
  end
  object CondPnl: TGridPanel
    AlignWithMargins = True
    Left = 3
    Top = 50
    Width = 820
    Height = 64
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
      end
      item
        Column = 2
        Control = HafsSW
        Row = 1
      end
      item
        Column = 3
        Control = Label4
        Row = 1
      end
      item
        Column = 4
        Control = DoneSW
        Row = 1
      end
      item
        Column = 5
        Control = Label5
        Row = 1
      end>
    RowCollection = <
      item
        Value = 50.000000000000000000
      end
      item
        Value = 50.000000000000000000
      end>
    ShowCaption = False
    TabOrder = 1
    object QuareesEdt: TEdit
      AlignWithMargins = True
      Left = 3
      Top = 3
      Width = 185
      Height = 26
      Align = alClient
      TabOrder = 0
      OnChange = ReadingEdtChange
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
      ExplicitWidth = 51
      ExplicitHeight = 18
    end
    object HafsSW: TToggleSwitch
      AlignWithMargins = True
      Left = 276
      Top = 35
      Width = 186
      Height = 26
      Align = alClient
      TabOrder = 3
      OnClick = DoneSWClick
      ExplicitLeft = 385
      ExplicitWidth = 77
      ExplicitHeight = 20
    end
    object Label4: TLabel
      AlignWithMargins = True
      Left = 468
      Top = 35
      Width = 76
      Height = 26
      Align = alClient
      Alignment = taCenter
      Caption = #1581#1601#1589
      Layout = tlCenter
      ExplicitWidth = 35
      ExplicitHeight = 18
    end
    object DoneSW: TToggleSwitch
      AlignWithMargins = True
      Left = 550
      Top = 35
      Width = 185
      Height = 26
      Align = alClient
      TabOrder = 4
      OnClick = DoneSWClick
      ExplicitLeft = 658
      ExplicitWidth = 77
      ExplicitHeight = 20
    end
    object Label5: TLabel
      AlignWithMargins = True
      Left = 741
      Top = 35
      Width = 76
      Height = 26
      Align = alClient
      Alignment = taCenter
      Caption = 'Done'
      Layout = tlCenter
      ExplicitWidth = 34
      ExplicitHeight = 18
    end
  end
  object StatPnl: TGridPanel
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
        Column = 1
        ColumnSpan = 2
        Control = StatusBar
        Row = 0
      end
      item
        Column = 3
        Control = HCountPnl
        Row = 0
      end
      item
        Column = 0
        Control = DCountPnl
        Row = 0
      end>
    RowCollection = <
      item
        Value = 100.000000000000000000
      end>
    ShowCaption = False
    TabOrder = 2
    object StatusBar: TPanel
      AlignWithMargins = True
      Left = 205
      Top = 0
      Width = 407
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
    object HCountPnl: TPanel
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
    end
    object DCountPnl: TPanel
      AlignWithMargins = True
      Left = 0
      Top = 0
      Width = 202
      Height = 25
      Margins.Left = 0
      Margins.Top = 0
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
      TabOrder = 2
    end
  end
  object ActnPnl: TGridPanel
    AlignWithMargins = True
    Left = 3
    Top = 508
    Width = 820
    Height = 41
    Align = alBottom
    BevelOuter = bvNone
    ColumnCollection = <
      item
        Value = 17.848691435696990000
      end
      item
        Value = 17.739003825193370000
      end
      item
        Value = 17.739003825193370000
      end
      item
        Value = 16.744458478718840000
      end
      item
        Value = 15.610676783737870000
      end
      item
        Value = 14.318165651459550000
      end>
    ControlCollection = <
      item
        Column = 2
        Control = UpdPnl
        Row = 0
      end
      item
        Column = 1
        Control = DecFontPnl
        Row = 0
      end
      item
        Column = 3
        Control = IncFontPnl
        Row = 0
      end
      item
        Column = 0
        Control = Panel1
        Row = 0
      end>
    RowCollection = <
      item
        Value = 100.000000000000000000
      end>
    ShowCaption = False
    TabOrder = 3
    OnDblClick = ActnPnlDblClick
    ExplicitLeft = -2
    object UpdPnl: TPanel
      AlignWithMargins = True
      Left = 295
      Top = 3
      Width = 139
      Height = 35
      Align = alClient
      BevelOuter = bvNone
      ShowCaption = False
      TabOrder = 0
      ExplicitLeft = 331
      ExplicitWidth = 158
      object UpdShp: TShape
        Left = 0
        Top = 0
        Width = 139
        Height = 35
        Align = alClient
        Pen.Color = 2823171
        Shape = stRoundRect
        ExplicitLeft = 48
        ExplicitTop = -16
        ExplicitWidth = 65
        ExplicitHeight = 65
      end
      object UpdateBtn: TSpeedButton
        Left = 0
        Top = 0
        Width = 139
        Height = 35
        Align = alClient
        Caption = 'Update Same'
        Flat = True
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -15
        Font.Name = 'Tahoma'
        Font.Style = [fsBold]
        ParentFont = False
        OnClick = UpdateBtnClick
        ExplicitLeft = 72
        ExplicitTop = 8
        ExplicitWidth = 23
        ExplicitHeight = 22
      end
    end
    object DecFontPnl: TPanel
      AlignWithMargins = True
      Left = 149
      Top = 3
      Width = 140
      Height = 35
      Align = alClient
      BevelOuter = bvNone
      ShowCaption = False
      TabOrder = 1
      ExplicitLeft = 167
      ExplicitWidth = 158
      object DecFontShp: TShape
        Left = 0
        Top = 0
        Width = 140
        Height = 35
        Align = alClient
        Pen.Color = 2823171
        Shape = stRoundRect
        ExplicitLeft = 48
        ExplicitTop = -16
        ExplicitWidth = 65
        ExplicitHeight = 65
      end
      object DecFontBtn: TSpeedButton
        Left = 0
        Top = 0
        Width = 140
        Height = 35
        Align = alClient
        Caption = '-- Font'
        Flat = True
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -15
        Font.Name = 'Tahoma'
        Font.Style = [fsBold]
        ParentFont = False
        OnClick = DecFontBtnClick
        ExplicitLeft = 72
        ExplicitTop = 8
        ExplicitWidth = 23
        ExplicitHeight = 22
      end
    end
    object IncFontPnl: TPanel
      AlignWithMargins = True
      Left = 440
      Top = 3
      Width = 132
      Height = 35
      Align = alClient
      BevelOuter = bvNone
      ShowCaption = False
      TabOrder = 2
      ExplicitLeft = 495
      ExplicitWidth = 158
      object IncFontShp: TShape
        Left = 0
        Top = 0
        Width = 132
        Height = 35
        Align = alClient
        Pen.Color = 2823171
        Shape = stRoundRect
        ExplicitLeft = 48
        ExplicitTop = -16
        ExplicitWidth = 65
        ExplicitHeight = 65
      end
      object IncFontBtn: TSpeedButton
        Left = 0
        Top = 0
        Width = 132
        Height = 35
        Align = alClient
        Caption = '++ Font'
        Flat = True
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -15
        Font.Name = 'Tahoma'
        Font.Style = [fsBold]
        ParentFont = False
        OnClick = IncFontBtnClick
        ExplicitTop = -3
      end
    end
    object Panel1: TPanel
      AlignWithMargins = True
      Left = 3
      Top = 3
      Width = 140
      Height = 35
      Align = alClient
      BevelOuter = bvNone
      ShowCaption = False
      TabOrder = 3
      ExplicitLeft = 11
      ExplicitTop = 6
      object Shape1: TShape
        Left = 0
        Top = 0
        Width = 140
        Height = 35
        Align = alClient
        Pen.Color = 2823171
        Shape = stRoundRect
        ExplicitLeft = 48
        ExplicitTop = -16
        ExplicitWidth = 65
        ExplicitHeight = 65
      end
      object SpeedButton1: TSpeedButton
        Left = 0
        Top = 0
        Width = 140
        Height = 35
        Align = alClient
        Caption = 'Refresh'
        Flat = True
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -15
        Font.Name = 'Tahoma'
        Font.Style = [fsBold]
        ParentFont = False
        OnClick = SpeedButton1Click
        ExplicitTop = 3
      end
    end
  end
  object HGrd: TDBGrid
    AlignWithMargins = True
    Left = 3
    Top = 120
    Width = 820
    Height = 120
    Align = alTop
    BorderStyle = bsNone
    DataSource = HDS
    DrawingStyle = gdsGradient
    FixedColor = 16766678
    GradientEndColor = 16766678
    GradientStartColor = 16766678
    TabOrder = 4
    TitleFont.Charset = DEFAULT_CHARSET
    TitleFont.Color = clWindowText
    TitleFont.Height = -15
    TitleFont.Name = 'Tahoma'
    TitleFont.Style = []
    OnColumnMoved = HGrdColumnMoved
  end
  object DGrd: TDBGrid
    AlignWithMargins = True
    Left = 3
    Top = 255
    Width = 820
    Height = 247
    Align = alClient
    BorderStyle = bsNone
    DataSource = DDS
    DrawingStyle = gdsGradient
    FixedColor = 16766678
    GradientEndColor = 16766678
    GradientStartColor = 16766678
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -32
    Font.Name = 'Sakkal Majalla'
    Font.Style = []
    ParentFont = False
    TabOrder = 5
    TitleFont.Charset = DEFAULT_CHARSET
    TitleFont.Color = clWindowText
    TitleFont.Height = -15
    TitleFont.Name = 'Tahoma'
    TitleFont.Style = []
    OnColumnMoved = DGrdColumnMoved
    OnKeyDown = DGrdKeyDown
  end
  object HQ: TADOQuery
    Connection = DB
    CursorType = ctDynamic
    CommandTimeout = 60000
    Parameters = <>
    SQL.Strings = (
      'SELECT ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS Sequence,'
      
        'reading, count(*) Count, group_concat(DISTINCT sub_subject) Subj' +
        'ect, '
      'group_concat(DISTINCT qarees) qarees FROM quran_data'
      'WHERE done IS NULL AND r5_2 IS NULL '
      'GROUP BY reading'
      'ORDER BY count(*) DESC')
    Left = 16
    Top = 64
    object HQSequence: TIntegerField
      FieldName = 'Sequence'
    end
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
    OnDataChange = HDSDataChange
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
    CursorType = ctDynamic
    CommandTimeout = 600000
    DataSource = HDS
    Parameters = <
      item
        Name = 'reading'
        Attributes = [paNullable, paLong]
        DataType = ftWideString
        Size = 65536
        Value = ''
      end>
    SQL.Strings = (
      
        'SELECT aya_index, id, sora, aya, sub_subject, qarees, reading, t' +
        'ags, '
      
        'page_number1, page_number2, readingresult, qareesrest, count_wor' +
        'ds, '
      'sub_sno, resultnew, wordsno, r5_2, done ,sub_subject1'
      'FROM quran_data'
      'where reading = :reading'
      'and'
      'r5_2 IS NULL'
      'and done is null')
    Left = 16
    Top = 112
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
    object DQsub_subject1: TWideMemoField
      FieldName = 'sub_subject1'
      BlobType = ftWideMemo
    end
    object DQresultnew: TWideMemoField
      DisplayLabel = 'Result New'
      FieldName = 'resultnew'
      BlobType = ftWideMemo
    end
    object DQtags: TWideMemoField
      DisplayLabel = 'Tags'
      DisplayWidth = 15
      FieldName = 'tags'
      BlobType = ftWideMemo
    end
    object DQqareesrest: TWideMemoField
      DisplayLabel = 'Qarees Rest'
      DisplayWidth = 45
      FieldName = 'qareesrest'
      BlobType = ftWideMemo
    end
    object DQDone: TIntegerField
      FieldName = 'Done'
    end
    object DQpage_number2: TIntegerField
      DisplayLabel = 'Page Number 2'
      FieldName = 'page_number2'
    end
    object DQreading: TWideMemoField
      DisplayLabel = 'Reading'
      DisplayWidth = 40
      FieldName = 'reading'
      BlobType = ftWideMemo
    end
    object DQreadingresult: TWideMemoField
      DisplayLabel = 'Reading Result'
      DisplayWidth = 15
      FieldName = 'readingresult'
      BlobType = ftWideMemo
    end
    object DQwordsno: TIntegerField
      DisplayLabel = 'Word SNo'
      FieldName = 'wordsno'
    end
  end
  object DB: TADOConnection
    ConnectionString = 
      #39'Provider=MSDASQL.1;Driver=SQLite3 ODBC Driver;Database=E:\Wursh' +
      'a\QeraatFasrhTools\QeraatSearch\qeraat_data_simple.db;'
    ConnectionTimeout = 600000
    LoginPrompt = False
    AfterConnect = DBAfterConnect
    Left = 16
    Top = 16
  end
  object Qry: TADOQuery
    Connection = DB
    CommandTimeout = 600000
    Parameters = <>
    Left = 48
    Top = 16
  end
end
