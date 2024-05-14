select page_number2,sora_name,aya,sub_subject,reading from all_qeraat where q3=1 and r5_2 is null
and reading not like '%مالة%'
and reading not like '%تقليل%'
and reading not like '%دغام%'
and reading not like '%دغم%'
and reading not like '%السورتين%'
and reading <>'بإسكان الهاء، مع ترك الوقف بهاء السكت.'
and reading <>'بكسر الهاء والميم وصلا، وبكسر الهاء وإسكان الميم وقفا.'
and reading not like '%مع الإدخال%'
and reading not like '%بتحقيق الهمزة الأولى،%'
and reading <>'بفتح ياء الإضافة.'
and reading <>'بفتح هاء التأنيث، مع الوقف عليها بالهاء.'
and reading <>'بتحقيق الهمزة، مع فتح هاء التأنيث، والوقف عليها بالهاء.'
order by aya_index,id