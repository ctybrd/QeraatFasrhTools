program TagsEditor;

uses
  Vcl.Forms,
  Master in 'Master.pas' {MasterF},
  DM in 'DM.pas' {DMF: TDataModule};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TMasterF, MasterF);
  Application.CreateForm(TDMF, DMF);
  Application.Run;
end.
