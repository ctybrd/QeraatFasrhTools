unit Master;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB,
  Vcl.Grids, Vcl.DBGrids, Vcl.Bind.Grid, Math, Vcl.ExtCtrls, Data.Win.ADODB,
  Vcl.StdCtrls, System.StrUtils, Vcl.ComCtrls, Vcl.Buttons, System.UITypes,
  Vcl.WinXCtrls;

type
  TMasterF = class(TForm)
    Spltr: TSplitter;
    HeadPnl: TPanel;
    HQ: TADOQuery;
    HQreading: TWideMemoField;
    HQcount: TIntegerField;
    HQsubject: TWideStringField;
    HQqarees: TWideStringField;
    HDS: TDataSource;
    DDS: TDataSource;
    DQ: TADOQuery;
    DQsora: TIntegerField;
    DQaya: TIntegerField;
    DQsub_subject: TWideMemoField;
    DQreading: TWideMemoField;
    DQtags: TWideMemoField;
    DQpage_number2: TIntegerField;
    DQreadingresult: TWideMemoField;
    DQqareesrest: TWideMemoField;
    DQresultnew: TWideMemoField;
    DQwordsno: TIntegerField;
    DQDone: TIntegerField;
    DB: TADOConnection;
    CondPnl: TGridPanel;
    QuareesEdt: TEdit;
    Label1: TLabel;
    SubjectEdt: TEdit;
    Label2: TLabel;
    ReadingEdt: TEdit;
    Label3: TLabel;
    StatPnl: TGridPanel;
    StatusBar: TPanel;
    HCountPnl: TPanel;
    Qry: TADOQuery;
    ActnPnl: TGridPanel;
    UpdPnl: TPanel;
    UpdShp: TShape;
    UpdateBtn: TSpeedButton;
    DecFontPnl: TPanel;
    DecFontShp: TShape;
    DecFontBtn: TSpeedButton;
    IncFontPnl: TPanel;
    IncFontShp: TShape;
    IncFontBtn: TSpeedButton;
    HGrd: TDBGrid;
    DGrd: TDBGrid;
    DCountPnl: TPanel;
    HafsSW: TToggleSwitch;
    Label4: TLabel;
    DoneSW: TToggleSwitch;
    Label5: TLabel;
    HQSequence: TIntegerField;
    DQsub_subject1: TWideMemoField;
    Panel1: TPanel;
    Shape1: TShape;
    SpeedButton1: TSpeedButton;
    procedure FormCreate(Sender: TObject);
    procedure DDSDataChange(Sender: TObject; Field: TField);
    procedure DBAfterConnect(Sender: TObject);
    procedure ReadingEdtChange(Sender: TObject);
    procedure UpdateBtnClick(Sender: TObject);
    procedure IncFontBtnClick(Sender: TObject);
    procedure DecFontBtnClick(Sender: TObject);
    procedure HGrdColumnMoved(Sender: TObject; FromIndex, ToIndex: Integer);
    procedure DGrdColumnMoved(Sender: TObject; FromIndex, ToIndex: Integer);
    procedure HDSDataChange(Sender: TObject; Field: TField);
    procedure DoneSWClick(Sender: TObject);
    procedure ActnPnlDblClick(Sender: TObject);
    procedure SpeedButton1Click(Sender: TObject);
    procedure DGrdKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
  private
    Procedure FilterHData();
    Procedure FilterDData();
    function AddAnd(Txt: String): String;
    procedure WideMemoGetText(Sender: TField; var Text: string;
      DisplayText: Boolean);
    procedure WideMemoSetText(Sender: TField; const Text: string);
    procedure AssignWideMemoFieldEvents(Qry: TADOQuery);
    { Private declarations }
    procedure OpenDSets;
  public
    { Public declarations }
  end;

var
  MasterF: TMasterF;
  Pth: String;
implementation

{$R *.dfm}

procedure TMasterF.FormCreate(Sender: TObject);

begin
  Pth := ExtractFileDir(
    ExtractFileDir(ExtractFileDir(
    ExtractFileDir(Application.ExeName)))) + '\qeraat_data_simple.db';
  StatusBar.Caption := Pth;

  DB.Connected := False;
  DB.ConnectionString := 'Provider=MSDASQL.1;Driver=SQLite3 ODBC Driver;'
    + 'Database=' + Pth + ';';

  try
    DB.Connected := True;
  except on e: Exception do
    ShowMessage('Error: ' + e.Message);
  end;
end;

procedure TMasterF.DBAfterConnect(Sender: TObject);
begin
  AssignWideMemoFieldEvents(HQ);
  AssignWideMemoFieldEvents(DQ);

  HQ.Open();
  DQ.Open();

  FilterHData();
  FilterDData();

  if FileExists('HGrd.ini') then
    HGrd.Columns.LoadFromFile('HGrd.ini');
  if FileExists('DGrd.ini') then
    DGrd.Columns.LoadFromFile('DGrd.ini');
end;

{$Region 'Grid Positions'}
procedure TMasterF.HGrdColumnMoved(Sender: TObject; FromIndex,
  ToIndex: Integer);
begin
  HGrd.Columns.SaveToFile('HGrd.ini');
end;

procedure TMasterF.DGrdColumnMoved(Sender: TObject; FromIndex,
  ToIndex: Integer);
begin
  DGrd.Columns.SaveToFile('DGrd.ini');
end;
procedure TMasterF.DGrdKeyDown(Sender: TObject; var Key: Word;
  Shift: TShiftState);
begin
  if key= VK_F3 then
    begin
      try
         DQ.edit;
      except

      end;
      DQ.fieldbyname('resultnew').asstring:=DQ.fieldbyname('sub_subject1').asstring;
    end;
end;

{$EndRegion}

{$Region 'Map Fields'}
procedure TMasterF.AssignWideMemoFieldEvents(Qry: TADOQuery);
var
  i: Integer;
  Field: TField;
begin
  for i := 0 to Qry.Fields.Count - 1 do
  begin
    Field := Qry.Fields[i];

    if Field.DataType = ftWideMemo then
    begin
      Field.OnGetText := WideMemoGetText;
      Field.OnSetText := WideMemoSetText;
    end;
  end;
end;

procedure TMasterF.WideMemoGetText(Sender: TField; var Text: string;
  DisplayText: Boolean);
begin
  Text := Sender.AsWideString;
end;

procedure TMasterF.WideMemoSetText(Sender: TField; const Text: string);
begin
  Sender.AsWideString := Text;
end;
{$EndRegion}

{$Region 'Filter Data'}
procedure TMasterF.ReadingEdtChange(Sender: TObject);
begin
  FilterHData();
end;

procedure TMasterF.SpeedButton1Click(Sender: TObject);
begin
  DBAfterConnect(DB);
end;

procedure TMasterF.DoneSWClick(Sender: TObject);
begin
//  FilterDData();
  OpenDSets;
end;

Procedure TMasterF.FilterHData();
var
  Fltr: String;
begin
  if ReadingEdt.Text <> '' then
    Fltr := 'reading like ' + QuotedStr('%' + ReadingEdt.Text + '%');

  if SubjectEdt.Text <> '' then
    Fltr := AddAnd(Fltr)
      + 'subject like ' + QuotedStr('%' + SubjectEdt.Text + '%');

  if QuareesEdt.Text <> '' then
    Fltr := AddAnd(Fltr)
      + 'qarees like ' + QuotedStr('%' + QuareesEdt.Text + '%');

  LockWindowUpdate(Handle);

  if Fltr = '' then
  begin
    HQ.Filtered := False;
    Exit;
  end;

  try
    HQ.Filtered := False;
    HQ.Filter := Fltr;
    HQ.Filtered := True;
  finally
    LockWindowUpdate(0);
    RedrawWindow(Handle, nil, 0, RDW_ERASE or RDW_FRAME or
      RDW_INVALIDATE or RDW_ALLCHILDREN);
  end;
end;

procedure TMasterF.FilterDData();
var
  Fltr: String;
begin
exit;
  if DoneSW.State = tssOff then
    Fltr := ''
  else
    Fltr := 'done = 1';

  if HafsSW.State = tssOff then
    Fltr := AddAnd(Fltr) + ''
  else
    Fltr := AddAnd(Fltr) + 'r5_2 = ' + QuotedStr('1');

  LockWindowUpdate(Handle);
  DQ.Filtered := False;
  if fltr<>'' then
  begin
  try
    DQ.Filter := Fltr;
    DQ.Filtered := True;
  finally
    LockWindowUpdate(0);
    RedrawWindow(Handle, nil, 0, RDW_ERASE or RDW_FRAME or
      RDW_INVALIDATE or RDW_ALLCHILDREN);
  end;
  end;
end;

procedure TMasterF.ActnPnlDblClick(Sender: TObject);
begin
 showmessage(hq.sql.text);
 showmessage(dq.sql.text);
end;

Function TMasterF.AddAnd(Txt: String): String;
begin
  Result := Ifthen(Txt <> '', Txt + ' And ', '');
end;
procedure TMasterF.OpenDSets;
var
  SQLH:string;
  SQLD:string;
  fltrALL:string;
begin
  fltrALL:='';
  if DoneSW.State <> tssOff then
    fltrALL := ' done = 1';

  if HafsSW.State <> tssOff then
    fltrALL := AddAnd(fltrALL) + ' r5_2 IS NULL';

  SQLH:='SELECT ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS Sequence,reading, count(*) Count,'+
  ' group_concat(DISTINCT sub_subject) Subject,'+
  ' group_concat(DISTINCT qarees) qarees FROM quran_data '+
   ifthen(fltrALL<>'',' WHERE '+fltrAll,'')+
   ' GROUP BY reading '+
  ' ORDER BY count(*) DESC ';

  SQLD :='SELECT aya_index, id, sora, aya, sub_subject, qarees, reading, tags,'+
  ' page_number1, page_number2, readingresult, qareesrest, count_words,' +
  'sub_sno, resultnew, wordsno, r5_2, done  FROM quran_data'+
  ' where reading = :reading '+
  ifthen(fltrALL<>'',' AND '+fltrAll,'');
  HQ.Filtered :=false;
  DQ.Filtered := False;

  DB.Connected := False;
  DB.ConnectionString := 'Provider=MSDASQL.1;Driver=SQLite3 ODBC Driver;'
    + 'Database=' + Pth + ';';

  try
    DB.Connected := True;
  except on e: Exception do
    ShowMessage('Error: ' + e.Message);
  end;
  DBAfterConnect(DB);
//
//  DQ.Close; // Make sure it's closed before executing
//  DQ.SQL.Clear; // Clear any previous SQL
//  DQ.SQL.Text := SQLD; // Assign new SQL
//
//  HQ.Close; // Make sure it's closed before executing
//  HQ.SQL.Clear; // Clear any previous SQL
//  HQ.SQL.Text := SQLH; // Assign new SQL
//
//  try
//    HQ.Open; // Activate the dataset
//  except
//    on E: Exception do
//      ShowMessage('Error opening dataset: ' + E.Message); // Catch the error
//  end;
//try
//  DQ.Open; // Activate the dataset
//except
//  on E: Exception do
//    ShowMessage('Error opening dataset: ' + E.Message); // Catch the error
//end;


end;
{$EndRegion}

{$Region 'Action Buttons'}
procedure TMasterF.UpdateBtnClick(Sender: TObject);
var
  SQL: String;
begin
  SQL := 'UPDATE quran_data ' +
    'SET resultnew = (Select a.resultnew ' +
    'FROM quran_data AS a ' +
    'WHERE NOT(a.resultnew IS NULL or a.resultnew = '''') ' +
    'AND a.sub_subject = quran_data.sub_subject ' +
    'AND a.reading = quran_data.reading) ' +
    'WHERE (quran_data.resultnew IS NULL or quran_data.resultnew='''')';

  Qry.SQL.Text := SQL;
  ShowMessage(SQL);

  if MessageDlg('Are you sure you want to update same records?',
    mtConfirmation, [mbYes, mbNo], 0) = mrYes then
  begin
    Qry.ExecSQL;
    HQ.Requery();
    DQ.Requery();
    ShowMessage('Done');
  end;
end;

procedure TMasterF.IncFontBtnClick(Sender: TObject);
begin
  Self.Font.Size := Self.Font.Size + 1;
  CondPnl.Height := CondPnl.Height + 3;
  HGrd.Font.Size := HGrd.Font.Size + 1;
  HGrd.TitleFont.Size := HGrd.Font.Size + 1;
  DGrd.Font.Size := DGrd.Font.Size + 1;
  DGrd.TitleFont.Size := HGrd.Font.Size + 1;
end;

procedure TMasterF.DecFontBtnClick(Sender: TObject);
begin
  Self.Font.Size := Self.Font.Size - 1;
  CondPnl.Height := CondPnl.Height - 3;
  HGrd.Font.Size := HGrd.Font.Size - 1;
  HGrd.TitleFont.Size := HGrd.Font.Size - 1;
  DGrd.Font.Size := DGrd.Font.Size - 1;
  DGrd.TitleFont.Size := HGrd.Font.Size - 1;
end;
{$EndRegion}

{$Region 'Record Count'}
procedure TMasterF.HDSDataChange(Sender: TObject; Field: TField);
begin
  if not HQ.IsEmpty then
    HCountPnl.Caption := Format('( %d : %d )', [HQ.RecNo, HQ.RecordCount])
  else
    HCountPnl.Caption := '( 0 : 0 )';
end;

procedure TMasterF.DDSDataChange(Sender: TObject; Field: TField);
begin
  if not DQ.IsEmpty then
    DCountPnl.Caption := Format('( %d : %d )', [DQ.RecNo, DQ.RecordCount])
  else
    DCountPnl.Caption := '( 0 : 0 )';
end;
{$EndRegion}

end.
