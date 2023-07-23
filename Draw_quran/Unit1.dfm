object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Form1'
  ClientHeight = 501
  ClientWidth = 678
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 35
    Top = 94
    Width = 33
    Height = 13
    Caption = 'Source'
  end
  object Label2: TLabel
    Left = 33
    Top = 139
    Width = 22
    Height = 13
    Caption = 'Dest'
  end
  object Image1: TImage
    Left = 408
    Top = 0
    Width = 270
    Height = 501
    Align = alRight
    Stretch = True
  end
  object src: TJvDirectoryEdit
    Left = 74
    Top = 91
    Width = 265
    Height = 21
    TabOrder = 0
    Text = 'E:\Qeraat\Draw_quran\pages'
  end
  object dest: TJvDirectoryEdit
    Left = 74
    Top = 136
    Width = 265
    Height = 21
    TabOrder = 1
    Text = 'E:\Qeraat\Draw_quran\pagesWA'
  end
  object Button1: TButton
    Left = 64
    Top = 200
    Width = 257
    Height = 89
    Caption = 'Start'
    TabOrder = 2
    OnClick = Button1Click
  end
  object Q: TRadioGroup
    Left = 1
    Top = 8
    Width = 401
    Height = 66
    Caption = #1575#1604#1602#1575#1585#1610#1569
    Columns = 5
    ItemIndex = 4
    Items.Strings = (
      #1602#1575#1604#1608#1606
      #1575#1576#1606' '#1603#1579#1610#1585
      #1575#1576#1608' '#1580#1593#1601#1585
      #1588#1593#1576#1577
      #1608#1585#1588)
    TabOrder = 3
  end
  object Lins: TADOQuery
    Connection = ADOConnection1
    Parameters = <>
    Left = 160
    Top = 352
  end
  object ADOQuery1: TADOQuery
    ConnectionString = 
      'Provider=SQLNCLI11.1;Integrated Security=SSPI;Persist Security I' +
      'nfo=False;User ID="";Initial Catalog=Shmrly_Lines;Data Source=.;' +
      'Initial File Name="";Server SPN=""'
    Parameters = <>
    Left = 320
    Top = 376
  end
  object ADOConnection1: TADOConnection
    ConnectionString = 
      'Provider=MSDASQL.1;Persist Security Info=False;Data Source=Shmrl' +
      'y'
    Provider = 'MSDASQL.1'
    Left = 336
    Top = 256
  end
end
