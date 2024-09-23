object DMF: TDMF
  OldCreateOrder = False
  OnCreate = DataModuleCreate
  Height = 495
  Width = 662
  object DB: TFDConnection
    Params.Strings = (
      
        'Database=E:\Wursha\QeraatFasrhTools\QeraatSearch\qeraat_data_sim' +
        'ple.db'
      'DateTimeFormat=DateTime'
      'DriverID=SQLite'
      'LockingMode=Normal')
    Connected = True
    LoginPrompt = False
    AfterConnect = DBAfterConnect
    Left = 32
    Top = 16
  end
  object Trans: TFDTransaction
    Connection = DB
    Left = 64
    Top = 16
  end
  object SQLite: TFDPhysSQLiteDriverLink
    Left = 96
    Top = 16
  end
  object Wait: TFDGUIxWaitCursor
    Provider = 'Forms'
    Left = 128
    Top = 16
  end
  object HeaderQ: TFDQuery
    Connection = DB
    FormatOptions.AssignedValues = [fvDefaultParamDataType, fvFmtDisplayDateTime, fvADOCompatibility]
    SQL.Strings = (
      
        'SELECT reading, count(*) count, group_concat(DISTINCT sub_subjec' +
        't) subject, '
      'group_concat(DISTINCT qarees) qarees'
      'FROM quran_data'
      'WHERE done IS NULL AND r5_2 IS NULL'
      'GROUP BY reading'
      'ORDER BY count(*) DESC')
    Left = 32
    Top = 72
    object HeaderQreading: TWideMemoField
      DisplayWidth = 50
      FieldName = 'reading'
      Origin = 'reading'
      BlobType = ftWideMemo
    end
    object HeaderQcount: TLargeintField
      AutoGenerateValue = arDefault
      FieldName = 'count'
      Origin = 'count'
      ProviderFlags = []
      ReadOnly = True
    end
    object HeaderQsubject: TWideStringField
      AutoGenerateValue = arDefault
      FieldName = 'subject'
      Origin = 'subject'
      ProviderFlags = []
      ReadOnly = True
      Size = 32767
    end
    object HeaderQqarees: TWideStringField
      AutoGenerateValue = arDefault
      FieldName = 'qarees'
      Origin = 'qarees'
      ProviderFlags = []
      ReadOnly = True
      Size = 32767
    end
  end
  object HeaderDS: TDataSource
    DataSet = HeaderQ
    Left = 64
    Top = 72
  end
  object DetailsQ: TFDQuery
    IndexFieldNames = 'reading'
    MasterSource = HeaderDS
    MasterFields = 'reading'
    Connection = DB
    FormatOptions.AssignedValues = [fvDefaultParamDataType, fvFmtDisplayDateTime]
    SQL.Strings = (
      
        'SELECT aya_index, id, sora, aya, sub_subject, qarees, reading, t' +
        'ags, '
      
        'page_number1, page_number2, readingresult, qareesrest, count_wor' +
        'ds, '
      'sub_sno, resultnew, wordsno, done '
      'FROM quran_data')
    Left = 32
    Top = 120
    object DetailsQaya_index: TIntegerField
      FieldName = 'aya_index'
      Origin = 'aya_index'
    end
    object DetailsQid: TIntegerField
      FieldName = 'id'
      Origin = 'id'
    end
    object DetailsQsora: TIntegerField
      FieldName = 'sora'
      Origin = 'sora'
    end
    object DetailsQaya: TIntegerField
      FieldName = 'aya'
      Origin = 'aya'
    end
    object DetailsQsub_subject: TWideMemoField
      DisplayWidth = 15
      FieldName = 'sub_subject'
      Origin = 'sub_subject'
      BlobType = ftWideMemo
    end
    object DetailsQqarees: TWideMemoField
      DisplayWidth = 50
      FieldName = 'qarees'
      Origin = 'qarees'
      BlobType = ftWideMemo
    end
    object DetailsQreading: TWideMemoField
      DisplayWidth = 50
      FieldName = 'reading'
      Origin = 'reading'
      BlobType = ftWideMemo
    end
    object DetailsQtags: TWideMemoField
      FieldName = 'tags'
      Origin = 'tags'
      BlobType = ftWideMemo
    end
    object DetailsQpage_number1: TIntegerField
      FieldName = 'page_number1'
      Origin = 'page_number1'
    end
    object DetailsQpage_number2: TIntegerField
      FieldName = 'page_number2'
      Origin = 'page_number2'
    end
    object DetailsQreadingresult: TWideMemoField
      DisplayWidth = 10
      FieldName = 'readingresult'
      Origin = 'readingresult'
      BlobType = ftWideMemo
    end
    object DetailsQqareesrest: TWideMemoField
      DisplayWidth = 50
      FieldName = 'qareesrest'
      Origin = 'qareesrest'
      BlobType = ftWideMemo
    end
    object DetailsQcount_words: TIntegerField
      FieldName = 'count_words'
      Origin = 'count_words'
    end
    object DetailsQsub_sno: TIntegerField
      FieldName = 'sub_sno'
      Origin = 'sub_sno'
    end
    object DetailsQresultnew: TWideMemoField
      FieldName = 'resultnew'
      Origin = 'resultnew'
      BlobType = ftWideMemo
    end
    object DetailsQwordsno: TIntegerField
      FieldName = 'wordsno'
      Origin = 'wordsno'
    end
    object DetailsQDone: TIntegerField
      FieldName = 'Done'
      Origin = 'Done'
    end
  end
  object DetailsDS: TDataSource
    DataSet = DetailsQ
    Left = 64
    Top = 120
  end
end
