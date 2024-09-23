unit DM;

interface

uses
  System.SysUtils, System.Classes, FireDAC.Stan.Intf, FireDAC.Stan.Option,
  FireDAC.Stan.Error, FireDAC.UI.Intf, FireDAC.Phys.Intf, FireDAC.Stan.Def,
  FireDAC.Stan.Pool, FireDAC.Stan.Async, FireDAC.Phys, FireDAC.Stan.ExprFuncs,
  FireDAC.Phys.SQLiteWrapper.Stat, FireDAC.Phys.SQLiteDef, FireDAC.VCLUI.Wait,
  FireDAC.Comp.UI, FireDAC.Phys.SQLite, FireDAC.Comp.Client, Data.DB, Vcl.Forms,
  Vcl.Dialogs, FireDAC.Stan.Param, FireDAC.DatS, FireDAC.DApt.Intf,
  FireDAC.DApt, FireDAC.Comp.DataSet;

type
  TDMF = class(TDataModule)
    DB: TFDConnection;
    Trans: TFDTransaction;
    SQLite: TFDPhysSQLiteDriverLink;
    Wait: TFDGUIxWaitCursor;
    HeaderQ: TFDQuery;
    HeaderDS: TDataSource;
    DetailsQ: TFDQuery;
    DetailsDS: TDataSource;
    HeaderQreading: TWideMemoField;
    HeaderQcount: TLargeintField;
    HeaderQsubject: TWideStringField;
    HeaderQqarees: TWideStringField;
    DetailsQaya_index: TIntegerField;
    DetailsQid: TIntegerField;
    DetailsQsora: TIntegerField;
    DetailsQaya: TIntegerField;
    DetailsQsub_subject: TWideMemoField;
    DetailsQqarees: TWideMemoField;
    DetailsQreading: TWideMemoField;
    DetailsQtags: TWideMemoField;
    DetailsQpage_number1: TIntegerField;
    DetailsQpage_number2: TIntegerField;
    DetailsQreadingresult: TWideMemoField;
    DetailsQqareesrest: TWideMemoField;
    DetailsQcount_words: TIntegerField;
    DetailsQsub_sno: TIntegerField;
    DetailsQresultnew: TWideMemoField;
    DetailsQwordsno: TIntegerField;
    DetailsQDone: TIntegerField;
    procedure DataModuleCreate(Sender: TObject);
    procedure DBAfterConnect(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  DMF: TDMF;

implementation

{%CLASSGROUP 'Vcl.Controls.TControl'}

{$R *.dfm}

procedure TDMF.DataModuleCreate(Sender: TObject);
var
  Pth: String;
begin
  Pth := ExtractFileDir(
    ExtractFileDir(
    ExtractFileDir(
    ExtractFileDir(Application.ExeName))))
    + '\qeraat_data_simple.db';

  DB.Connected := False;
  DB.Params.Database := Pth;
  DB.Connected := True;

  try
    DB.Connected := True;
  except
    ShowMessage('Error DB Path: ' + Pth);
  end;
end;

procedure TDMF.DBAfterConnect(Sender: TObject);
begin
  HeaderQ.Open();
  DetailsQ.Open();
end;

end.
