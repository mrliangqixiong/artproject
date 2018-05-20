from django.db import models

# Create your models here.
from django.utils import timezone
from DjangoUeditor.models import UEditorField

class Tag(models.Model):
	t_name = models.CharField(max_length=255, verbose_name="标签名")
	t_info = models.CharField(max_length=300, verbose_name="描述")
	t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建日期")

	def __str__(self):
		return self.t_name

	class Meta:
		verbose_name = "标签信息"
		verbose_name_plural = '标签信息'



class Art(models.Model):
	a_title = models.CharField(max_length=255, verbose_name="文章标题")
	a_info = models.CharField(max_length=500, verbose_name="备注")
	#a_content = models.TextField(verbose_name="文章内容")
	a_content = UEditorField(verbose_name="文章内容", width=1000, height=600,
							 imagePath="static/uploads/", filePath="static/uploads/",
							 blank=True, toolbars="full")
	a_img = models.ImageField(null=True, blank=True,
							  upload_to="uploads", verbose_name="文章图片")
	a_addtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")
	a_updatetime = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
	a_tag = models.ForeignKey(Tag)   #a_tag_id


	def __str__(self):
		return self.a_title

	class Meta:
		verbose_name = "美文信息"
		verbose_name_plural = '美文信息'
		ordering = ['-a_addtime']
		
		
		
		
		
		